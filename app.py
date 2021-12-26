import telebot
from telebot import types
from telebot.types import Message
from tester import test

TOKEN = '1788557128:AAHCbluR52mTv3heI89pFt9dtA5JTXqMQXU'
bot = telebot.TeleBot(TOKEN)
# user = bot.get_me()
# print(user)


@bot.message_handler(commands=['start_speedtest'])
def command_handler(message: Message):
    #bot.reply_to(message, 'Получение результата...')
    
    try:
        bot.reply_to(message, 'Получение оптимального сервера')
        a = test.get_best_server()
        srvr = a['host'], a['name'], a['country']
        bot.reply_to(message, srvr)
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')
        
    try:
        bot.reply_to(message, 'Получение скорости скачивания...')
        download_result = test.download() / 1024 / 1024
        bot.reply_to(message, f'Donload result: {"%.2f" % download_result}/Mbit.')
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')
    
    try:
        bot.reply_to(message, 'Получение скорости загрузки...')
        upload_result = test.upload() / 1024 / 1024
        bot.reply_to(message, f'Upload_result: {"%.2f" % upload_result}/Mbit.')
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')


bot.polling(timeout=30)    
