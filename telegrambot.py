from urllib import request
import json


class TelegramBot:
    def __init__(self, token):
        self.TOKEN = token
        self.__limit = 100
        self.__timeout = 0

    def getme(self):
        botinfo = json.loads(request.urlopen('https://api.telegram.org/bot{0}/getMe'.format(self.TOKEN)).
                             read().decode('utf-8'))
        return botinfo['result']

    def getupdates(self, offset='', limit='', timeout='', allowed_updates=''):
        update = json.loads(request.urlopen(
            f'https://api.telegram.org/bot{self.TOKEN}/getUpdates?offset={offset}&'
            f'limit='f'{limit}&timeout={timeout}&allowed_updates={allowed_updates}').read().decode('utf-8'))
        if update['ok']:
            updates = []
            for update in update['result']:
                updates.append(Update(update))
            return updates
        else:
            print('Not OK')

    def sendmessage(self, chat_id, text, parse_mode="", disable_web_page_preview=True,
                    disable_notification=True, reply_to_message_id="", reply_markup=""):
        return request.urlopen(f'https://api.telegram.org/bot{self.TOKEN}/sendMessage?chat_id={chat_id}&'
                               f'text=' + request.quote(text) + f'&parse_mode={parse_mode}&'
                               f'disable_web_page_preview={disable_web_page_preview}&'
                               f'disable_notification={disable_notification}&reply_to_message_id={reply_to_message_id}&'
                               f'reply_markup={reply_markup}')


class TelegramMessage:
    def __init__(self, msg):
        self.__msg = msg

    @property
    def message_id(self):
        return self.__msg['message_id']

    @property
    def from_user(self):
        return TelegramUser(self.__msg['from'])

    @property
    def chat(self):
        return TelegramChat(self.__msg['chat'])

    @property
    def date(self):
        return self.__msg['date']

    @property
    def text(self):
        if "text" in self.__msg:
            return self.__msg['text']
        else:
            return None


class TelegramChat:
    def __init__(self, chat):
        self.__chat = chat

    @property
    def id(self):
        return self.__chat['id']


class TelegramUser:
    def __init__(self, user):
        self.__user = user


class Update:
    def __init__(self, upd):
        self.__update = upd

    @property
    def update_id(self):
        return self.__update['update_id']

    @property
    def message(self):
        return TelegramMessage(self.__update['message'])

    def __str__(self):
        return 'Update ID: ' + str(self.__update['update_id'])

    def __repr__(self):
        return 'Update ID: ' + str(self.__update['update_id'])







