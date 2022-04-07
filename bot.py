#Імпорти

import telebot
import requests
from bs4 import BeautifulSoup as BS

#Запуск

print ("Бот запущений")

#Змінні

bot = telebot.TeleBot('5113147431:AAGA6l6jT4E1cRX9S2Sbs32I9cXY51XZJ6M')

city = ''


#Діалог

@bot.message_handler (content_types=['text'])
def b (message):
    if message.text == 'Путін':
        bot.reply_to(message, 'ХУЙЛО!')

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
