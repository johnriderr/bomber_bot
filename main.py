import config
import telebot
from telebot import types
from db import session, Client
from spamthreads import SpamThread, SpamThreadsDaddy
from random import randint
import requests
import json
from datetime import timedelta
from datetime import datetime
from math import ceil
import daemon

bot = telebot.TeleBot(config.token)

spam_threads = SpamThreadsDaddy()
spam_threads.start()

kiwi_data_cash = None
kiwi_data_cash_updated = None


@bot.message_handler(content_types=["text"])
def any_msg(message):
    client = create_client_in_db_if_not_exist(message.chat.id)
    if (message.text[:2] == '38' and len(message.text) == 12) or\
            (message.text[:2] == '79' and len(message.text) == 11):  # if message.text is a number
        if client.spam_balance >= 1:
            if not spam_threads.is_spamming(client, message.text):
                bot.send_message(message.chat.id, 'Начинаем спам', reply_markup=markup_main_menu())
                new_spam_thread = SpamThread(phone=message.text, client=client, session=session, spam_iterations=20)
                new_spam_thread.start()
                spam_threads.add_thread(new_spam_thread)
            else:
                bot.send_message(message.chat.id, 'Спам уже идет', reply_markup=markup_main_menu())
        else:
            bot.send_message(message.chat.id, 'Пополните ваш баланс', reply_markup=markup_main_menu())
    elif message.text == 'Начать Спам':
        bot.send_message(message.chat.id, '''Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx''',
                         reply_markup=markup_main_menu())
    elif message.text == 'Остановить Спам':
        if not spam_threads.is_spamming(client):
            bot.send_message(message.chat.id, text='От вас нет спама', reply_markup=markup_main_menu())
        else:
            spam_threads.stop_spam(client)
            bot.send_message(message.chat.id, text='Спам остановлен', reply_markup=markup_main_menu())
    elif message.text == 'Проверить/Обновить Баланс':
        global kiwi_data_cash_updated
        if not kiwi_data_cash_updated or datetime.now() - kiwi_data_cash_updated > timedelta(seconds=5):
            resp = payment_history_last(config.kiwi_login, config.kiwi_api_access_token, 25, '', '')
            kiwi_data_cash_updated = datetime.now()
            for payment in resp['data']:
                client_to_pay = session.query(Client).filter_by(payment_comment=payment['comment']).first()
                if client_to_pay:
                    client_to_pay.payment_comment = 0
                    client_to_pay.spam_balance += ceil(float(payment['sum']['amount']))
                    session.commit()
                    bot.send_message('244759337', text='Покупка на: {} рублей'.format(
                        ceil(float(payment['sum']['amount']))))  # to me
                    bot.send_message('338115019', text='Покупка на: {} рублей'.format(
                        ceil(float(payment['sum']['amount']))))  # to panda
        bot.send_message(message.chat.id, text='Ваш баланс: {} рублей'.format(client.spam_balance), reply_markup=markup_main_menu())
    elif message.text == 'Пополнить Баланс':
        # bot.send_message(message.chat.id, text='Доступные тарифы', reply_markup=markup_main_menu())
        a, b = 1000, 9999
        pay_comm = randint(a, b)
        while session.query(Client).filter_by(payment_comment=pay_comm).first():
            pay_comm = randint(a, b)
        client.payment_comment = pay_comm
        session.commit()
        bot.send_message(message.chat.id,
                         text='Оправьте сумму от 20 рублей на QIWI +{} с комментарием {}\n\nПосле оплаты обновите бала нс - Проверить/Обновить Баланс'.format(
                             config.kiwi_login, client.payment_comment), reply_markup=markup_main_menu())
    elif message.text == 'Информация':
        bot.send_message(message.chat.id,
                         text='Кодер: @john_riderr\nОснователь: @Pa3eTkA1703\nбеседа: @terasoftb'.format(
                             client.spam_balance), reply_markup=markup_main_menu())
    elif message.text == 'Информация':
        bot.send_message(message.chat.id,
                         text='Кодер: @john_riderr\nОснователь: @Pa3eTkA1703\nбеседа: @terasoftb'.format(
                             client.spam_balance), reply_markup=markup_main_menu())
    else:
        print(message.text)
        bot.send_message(message.chat.id, text='Choose button', reply_markup=markup_main_menu())
    print('query from:', message.from_user.id)


def create_client_in_db_if_not_exist(tg_id):
    client = session.query(Client).filter_by(tg_id=tg_id).first()
    new_client = None
    if not client:
        new_client = Client(spam_balance=15, tg_id=tg_id, payment_comment=0)
        session.add(new_client)
        session.commit()
    return client if client else new_client


def markup_main_menu():
    markup = types.ReplyKeyboardMarkup(row_width=8, resize_keyboard=True)
    button_start_spam = types.KeyboardButton('Начать Спам')
    button_stop_spam = types.KeyboardButton('Остановить Спам')
    check_spam_status = types.KeyboardButton('Проверить/Обновить Баланс')
    button_add_balance = types.KeyboardButton('Пополнить Баланс')
    button_info = types.KeyboardButton('Информация')
    markup.add(button_start_spam, button_stop_spam)
    markup.add(check_spam_status, button_add_balance)
    markup.add(button_info)
    return markup


def payment_history_last(my_login, api_access_token, rows_num, next_TxnId, next_TxnDate):
    s = requests.Session()
    s.headers['authorization'] = 'Bearer ' + api_access_token
    parameters = {'rows': rows_num, 'nextTxnId': next_TxnId, 'nextTxnDate': next_TxnDate}
    h = s.get('https://edge.qiwi.com/payment-history/v2/persons/' + my_login + '/payments', params=parameters)
    # print('kiwi response:', h)
    return json.loads(h.text)


if __name__ == '__main__':
    daemon_mode = False
    if daemon_mode:
        with daemon.DaemonContext():
            bot.polling(none_stop=True)
    else:
        bot.polling(none_stop=True)
