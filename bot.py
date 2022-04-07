#Імпорти

import telebot
import requests
from bs4 import BeautifulSoup as BS
import time
from telebot import apihelper

#Запуск

print ("Бот запущений")

#Змінні

bot = telebot.TeleBot('5101895600:AAGJyHn0GFtQEVlcxYHP3ptOV1X8NV0_qQA')

city = ''

#Діалог

@bot.message_handler (content_types=['text'])
def b (message):
    if message.text == 'Путін':
        bot.reply_to(message, 'КОНЧЕНИЙ!')
        time.sleep(1)
        bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEZS5iTiHioxvQHOzRv-63xOLOSjQsUAACFQADDjpEJlqB3UqNRBwCIwQ')
    if message.text == "кік":
        idd = message.reply_to_message.from_user.id
        bot.kick_chat_member(message.chat.id, idd)
    if message.text == 'Юзерс':
        pars = bot.get_chat_members_count(message.chat.id)
        bot.send_message(message.chat.id, pars)
    if message.text == 'ID':
        chat = message.chat.id
        bot.send_message(message.chat.id, chat)


    #Інформація про Юзера

    user_message = message.text
    user_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_nickname = message.from_user.username

    #Шпійонство

    if user_last_name:
        print(user_name,user_last_name,"(",user_nickname,")",": ",user_message)
    else:
        print(user_name,"( @",user_nickname,")"": ",user_message)


    #Введіть Місто

    if message.text.lower() == 'погода':
       bot.reply_to(message, 'Будь ласка, введіть місто, погоду у якому ви хочете дізнатися')

    else:

       #Перетворення

       city = message.text
       split = city.split()
       city_ok = '-'.join(split)

       #Запрос

       url = 'https://ua.sinoptik.ua/погода-' + city_ok
       r = requests.get(url)
       html = BS(r.content, 'html.parser')

      #Пошук

       for el in html.select('#content'):
           t_min = el.select('.temperature .min')[0].text
           t_max = el.select('.temperature .max')[0].text
           text = el.select('.wDescription .description')[0].text

       #Антикраш

       valid = requests.get(url)

       if 'Погода' in user_message:
           if valid:
               bot.reply_to(message, text + '\n \n' + "Температура: " + t_min + ", " + t_max)
           else:
               bot.reply_to(message, "Вибачте, але я не знаю такого міста :(")

#Цикл

bot.polling(none_stop=True)
