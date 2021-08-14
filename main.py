
from decouple import config
import telebot

API_KEY = config('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['greet'])
def greet(message):
    bot.reply_to(message, "Hey!How's it going?")

#Reply with the same message sent to the person
@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)


# This won't be sent as a reply to the command
@bot.message_handler(commands=['hello'])
def hello(message):
    bot.send_message(message.chat.id, "Hello!")

bot.polling()


