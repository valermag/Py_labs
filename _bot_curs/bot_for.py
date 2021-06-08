import telebot
bot = telebot.TeleBot('1813110218:AAEnX0F05XQLEDeQhWa4bNaZZIiHElMWQXQ')
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id, "")
bot.polling()