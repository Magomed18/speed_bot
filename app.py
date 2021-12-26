import telebot
from telebot import types
from telebot.types import Message
from tester import test, download_result, upload_result


TOKEN = '1788557128:AAHCbluR52mTv3heI89pFt9dtA5JTXqMQXU'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start_speedtest'])
def command_handler(message: Message):

    try:
        bot.reply_to(message, 'Получение оптимального сервера')
        s = test.get_best_server()
        bot.reply_to(message, f"Найден: {s['host']} расположен в {s['name']}, {s['country']}.")
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')
    try:
        bot.reply_to(message, 'Получение скорости скачивания...')
        #download_result = test.download() / 1024 / 1024
        bot.reply_to(message, f'Download result: {"%.2f" % download_result}/Mbit.')
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')
    try:
        bot.reply_to(message, 'Получение скорости загрузки...')
        #upload_result = test.upload() / 1024 / 1024
        bot.reply_to(message, f'Upload_result: {"%.2f" % upload_result}/Mbit.')
    except Exception:
        bot.reply_to(message, 'Извините, произошла ошибка при получении данных')


bot.polling(timeout=30)    


