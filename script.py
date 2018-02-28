import telegrambot
import weatherparser

TOKEN = ''
update_offset = 0
bot = telegrambot.TelegramBot(TOKEN)
NO_TEXT_MSG = 'Не понятно, что это такое вообще вы шлете.'
START_MSG = 'Отправьте название города, чтобы узнать температуру.'
UNKNOWN_COMMAND_MSG = 'Неизвестная команда.'
STOP_CHARS = (';', '.', ':', '\'', '\"', '/', '\\', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0')

while True:
    updates = bot.getupdates(update_offset)
    print(updates)

    for update in updates:
        update_offset = update.update_id + 1
        if update.message.text:
            for char in STOP_CHARS:
                if char in update.message.text:
                    bot.sendmessage(update.message.chat.id, NO_TEXT_MSG)
                    break
                else:
                    if update.message.text[0] == '/':
                        if update.message.text == '/start':
                            bot.sendmessage(update.message.chat.id, START_MSG)
                        else:
                            bot.sendmessage(update.message.chat.id, UNKNOWN_COMMAND_MSG)
                        break
                    else:
                        bot.sendmessage(update.message.chat.id, weatherparser.getweather(update.message.text))
                        break
        else:
            bot.sendmessage(update.message.chat.id, NO_TEXT_MSG)
