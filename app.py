import telebot
import requests
from telebot import types
from telebot.types import Message
from tester import test

TOKEN = '1788557128:AAHCbluR52mTv3heI89pFt9dtA5JTXqMQXU'
# URL = f'https://api.telegram.org/bot{TOKEN}'
# a = requests.get(f'{URL}/getMe')
# print(a.json())
bot = telebot.TeleBot(TOKEN)
user = bot.get_me()
print(user)


@bot.message_handler(commands=['start_speedtest'])
def command_handler(message: Message):
    bot.reply_to(message, 'Получение результата...')
    download_result = test.download() / 1024 / 1024
    upload_result = test.upload() / 1024 / 1024

    bot.reply_to(message, f'Donload result: {"%.2f" % download_result}/Mbit.\nUpload_result: {"%.2f" % upload_result}/Mbit.')
    


bot.polling(timeout=30)    
