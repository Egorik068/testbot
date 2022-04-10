import telebot
import re
import config
import os
import traceback
import requests
from bs4 import BeautifulSoup as BS
from pathlib import Path

bot = telebot.TeleBot(config.token)

#

@bot.message_handler(content_types=['new_chat_members'])
def delete_jf(message):
    bot.delete_message(message.chat.id, message.message_id)
    usbn = message.from_user.id
    with open('USERS.txt', 'a') as new_users:
        new_users.write(str(usbn) + "\n")
    with open('BANS.txt', 'r') as banned:
        users_ban = banned.read()
    bot.kick_chat_member(message.chat.id, users_ban)

#

@bot.message_handler(commands=['ban'])
def bans(message):
    banik = message.text
    uimb = message.from_user.id
    adm = bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    adm = adm.status
    if adm == "creator" or adm == "administrator":
        if message.reply_to_message:
            chat_ids = message.reply_to_message.from_user.id
            tt = message.text
            id_ban = message.reply_to_message.from_user.id
            bot.ban_chat_member(message.chat.id, id_ban, 222222222222222222)
            with open('BANS.txt', 'a') as banned:
                    banned.write(str(id_ban) + "\n")
        if message.reply_to_message is None:
            return bot.reply_to(message, "Вам потрібно відповісти на повідомлення людини, яку хочете забанити :)")
    else:
        bot.reply_to(message, "В тебе нема прав банити людей :(")

#

@bot.message_handler(commands=['kick'])
def adm (message):
           adm = bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
           adm = adm.status
           if adm == "creator" or adm == "administrator":
               if message.reply_to_message:
                   id_kik = message.reply_to_message.from_user.id
                   bot.kick_chat_member(message.chat.id, id_kik)
               else:
                    bot.reply_to(message, "Вам потрібно відповісти на повідомлення людини, яку хочете кікнути :)")
           else:
               bot.reply_to(message, "В тебе нема прав виганяти людей :(")

#

@bot.message_handler(content_types=['text'])
def msg(message):
    if message.text == 'РП':
        bot.reply_to(message, '''
в нас є такі команди як:
/kick - для адміністраторів чату
/ban - для адміністраторів чату
і всякі приколюхи по типу:
1)вдарити  10)уєбати
2)облизати  11)обісрати
3)покормити  12)виєбати
4)обняти
5)зїсти
6)вкусити
7)вбити
8)каструвати
9)погладити
Ще у нас є унікальна команда завдяки якій ви можете дізнатися погоду в свому місті!!
Погода і ваше місто :)
приклад: Погода львів
        ''')
    if message.reply_to_message:
            a = message.from_user.first_name
            b = message.from_user.id
            d = message.reply_to_message.from_user.id
            c = message.reply_to_message.from_user.first_name

            if message.text.lower() == "вдарити":
                bot.send_message(message.chat.id, f"😵‍💫🥊| [{a}](tg://user?id={b}) вдарив [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "облизати":
                bot.send_message(message.chat.id, f"😋🤤| [{a}](tg://user?id={b}) облизав [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "покормити":
                bot.send_message(message.chat.id, f"🍪🥞| [{a}](tg://user?id={b}) покормив [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "обняти":
                bot.send_message(message.chat.id, f"☺️🤗| [{a}](tg://user?id={b}) обняв [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "зїсти":
                bot.send_message(message.chat.id, f"👩‍🍳🦃| [{a}](tg://user?id={b}) з'їв [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "вкусити":
                bot.send_message(message.chat.id, f"🤨😬| [{a}](tg://user?id={b}) вкусив [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "вбити":
                bot.send_message(message.chat.id, f"😡🔪| [{a}](tg://user?id={b}) вбив [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "каструвати":
                bot.send_message(message.chat.id, f"🥚🐣| [{a}](tg://user?id={b}) кастрував [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "погладити":
                bot.send_message(message.chat.id, f"🥰☺️| [{a}](tg://user?id={b}) погладив [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "уєбати":
                bot.send_message(message.chat.id, f"😡👊| [{a}](tg://user?id={b}) уєбав [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "обісрати":
                bot.send_message(message.chat.id, f"🤭💩| [{a}](tg://user?id={b}) обісрати [{c}](tg://user?id={d})", parse_mode='Markdown')

            if message.text.lower() == "виєбати":
                bot.send_message(message.chat.id, f"👉👌😬| [{a}](tg://user?id={b}) змусив до жорсткого інтиму [{c}](tg://user?id={d})", parse_mode='Markdown')

    text = message.text
    adms = bot.get_chat_member(chat_id=message.chat.id, user_id=message.from_user.id)
    adms = adms.status
    if adms == "creator" or adms == "administrator":
        if message.reply_to_message:
            if message.text == 'Розбан':
                reprosban = message.reply_to_message.id
                Path('BANS.txt').write_text(Path('BANS.txt').read_text().replace('5120511081', ''))
                bot.reply_to(message, 'Юзер розбанений!')

#Чек чи є у нас порушники

        if message.text == 'Чек':
            with open('BANS.txt', 'r') as banned:
                users_ban = banned.read()
            bot.kick_chat_member(message.chat.id, users_ban)


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

        if 'Погода' in message.text:
            if valid:
                bot.reply_to(message, text + '\n \n' + "Температура: " + t_min + ", " + t_max)
            else:
                bot.reply_to(message, "Вибачте, але я не знаю такого міста :(")


bot.polling(none_stop=True)
