#The test bot

import requests
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler, Filters


updater = Updater(token='1825942069:AAHhJsxw7msxE2beYDQcCsBr4nPjBLnl6K4', use_context=True)

dispatcher = updater.dispatcher


def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Привет, я бот погоды")
    context.bot.send_message(chat_id=update.effective_chat.id, text="Введи город, чтобы узнать погоду в нем")

def get_weather(update, context):
    weather = requests.get(f'https://wttr.in/{update.message.text}?format=3')
    context.bot.send_message(chat_id=update.effective_chat.id, text=weather.text)


city_message_handler = MessageHandler(Filters.text & (~Filters.command), get_weather)
dispatcher.add_handler(city_message_handler)

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)


updater.start_polling()
updater.idle()