import random
from random import choice
import telebot
from telebot import types

TOKEN = '#token'
bot = telebot.TeleBot(TOKEN)

compliments = ['compliment1', 'compliment2', 'compliment3']

@bot.message_handler(commands=['start']) # handle '/start' message when user starts Bank Banger bot

def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True) # 'markup' is a keyboard
    # buttons
    item1 = types.KeyboardButton('Напиши комплимент для woman <3')
    # add buttons to markup
    markup.add(item1)
    # welcome message
    bot.send_message(message.chat.id, 'Привет, woman <3 Чем могу помочь?', reply_markup = markup)

@bot.message_handler(content_types=['text']) # handle every text information from user

def send_message(message): # responses
    if message.chat.type == 'private':
        if message.text == 'Напиши комплимент для woman <3':
            bot.send_message(message.chat.id, (random.choice(compliments)))

bot.polling(none_stop = True) # keeps bot online

# qty = len(compliments)
# print(qty)
