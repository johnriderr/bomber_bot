import config
import telebot
from telebot import types
from bomber import start_spam
from db import session, Client
from spamthreads import SpamThread, SpamThreadsDaddy

bot = telebot.TeleBot(config.token)

spam_threads = SpamThreadsDaddy()
spam_threads.start()


@bot.message_handler(content_types=["text"])
def any_msg(message):
    markup = make_murkup()
    client = create_client_in_db_if_not_exist(message.chat.id)
    if len(message.text) == 12:
        if message.text[:2] == '38' or message.text[:2] == 79: # if message.text is a number
            if client.spam_balance > 5:
                if not spam_threads.is_spamming(client, message.text):

                    bot.send_message(message.chat.id, 'Начинаем спам', reply_markup=markup)
                    new_spam_thread = SpamThread(phone=message.text, client=client, spam_iterations=20)
                    new_spam_thread.start()
                    spam_threads.add_thread(new_spam_thread)
                else:
                    bot.send_message(message.chat.id,                                     'Спам уже идет',                                     reply_markup=markup)
            else:
                bot.send_message(message.chat.id, 'Пополните ваш баланс', reply_markup=markup)

    elif message.text == 'Начать Спам':
        bot.send_message(message.chat.id, '''Введите номер без + в формате:\n🇺🇦 380xxxxxxxxx\n🇷🇺 79xxxxxxxxx''',
                         reply_markup=markup)
    elif message.text == 'Остановить Спам':
        spam_threads.stop_spam(client)
    else:
        bot.send_message(message.chat.id, text='Choose button', reply_markup=markup)

    print(message.from_user.id)


def create_client_in_db_if_not_exist(tg_id):
    client = session.query(Client).filter_by(tg_id=tg_id).first()
    new_client = None
    if not client :
        new_client = Client(spam_balance=0, tg_id=tg_id, payment_comment=25)
        session.add(new_client)
        session.commit()
    return client if client else new_client


def make_murkup():
    markup = types.ReplyKeyboardMarkup(row_width=2)
    button_start_spam = types.KeyboardButton('Начать Спам')
    button_stop_spam = types.KeyboardButton('Остановить Спам')
    check_spam_status = types.KeyboardButton('пр')
    markup.add(button_start_spam, button_stop_spam)
    return markup


if __name__ == '__main__':
    bot.polling(none_stop=True)