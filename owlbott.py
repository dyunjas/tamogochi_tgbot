import telebot
import random
from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from telebot import types
bot = telebot.TeleBot('7087882100:AAEGfcvee1sBeIJPfpMFGfUd5XmIZ8-yV5Q')


money = 50
energy = 50
happiness = 50
satiety = 50
names = ['Совушка', 'Совунья', 'Софа', 'Букля']
name = random.choice(names)
lvl = 0
points = 0




@bot.message_handler(commands=['start'])
def set_reminder(message):
    global money, energy, happiness, satiety, name, lvl, points
    money = 50
    energy = 50
    happiness = 50
    satiety = 50
    name = random.choice(names)
    lvl = 0
    points = 0
    chat_id = message.chat.id
    bot.send_message(chat_id, 'Здравствуйте, для запуска игры напишите команду [ /play_1 ]. Имя для вашей совы будет выбрано рандомно!')


@bot.message_handler(commands=['play_1'])
def button1_message(message):
   markup = ReplyKeyboardMarkup(resize_keyboard=True)
   button1 = KeyboardButton(text='Еда')
   button2 = KeyboardButton(text='Сон')
   button3 = KeyboardButton(text='Прогулка')
   button4 = KeyboardButton(text='Тренировка')
   button5 = KeyboardButton(text='Информация о питомце')
   button6 = KeyboardButton(text='Заработок монет')
   button7 = KeyboardButton(text='Уровень питомца')
   button8 = KeyboardButton(text='Магазин')
   markup.add(button1, button2, button3, button4, button5, button6, button7, button8)
   bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

def stats_pet(message):
   chat_id = message.chat.id
   bot.send_message(chat_id,f'''Кол-во денег:{money}
Уровень голода:{satiety}
Уровень энергии:{energy}
Уровень счастья:{happiness}
Очки опыта питомца:{points}''')

def check(message):
    death = False
    global satiety, energy, happiness, name
    if satiety <= 0:
        death = True
        bot.send_message(message.chat.id, f'{name} умер от голода. Не забывайте кормить питомца!')
    elif satiety >= 10:
        bot.send_message(message.chat.id, f'{name} наелся и счастлив!')
    if happiness < 0:
        death = True
        bot.send_message(message.chat.id, f'{name} умер от тоски. С питомцем нужно чаще играть!')
    elif happiness > 100:
        bot.send_message(message.chat.id, f'{name} счастлив как никогда')
    if energy < 0:
        death = True
        bot.send_message(message.chat.id, f'{name} умер от усталости. Питомцу нужно давать отдыхать!')
    elif energy > 100:
        bot.send_message(message.chat.id, f'{name} полон сил')
    if death:
        chat_id = message.chat.id
        photo = open(r"Снимок экрана 2024-07-12 204849.png", 'rb')
        bot.send_photo(chat_id, photo=photo)
        bot.send_message(message.chat.id, 'Игра начинается заново!')
        set_reminder(message)



@bot.message_handler(func=lambda message: message.text in ['Еда', 'Сон', 'Игра', 'Тренировка', 'Прогулка', 'Поинты' ])
def game_handler(message):
    global  money, energy, happiness, satiety, points, lvl
    if message.text == 'Еда':
        chat_id = message.chat.id
        photo = open(r"Снимок экрана 2024-07-12 174340.png", 'rb')
        bot.send_photo(chat_id, photo=photo)
        satiety+=25
        money-=5
        energy+=25
        points+=1
        check(message)
        stats_pet(message)

    elif message.text =='Сон':
        satiety-=50
        happiness+=25
        energy+=50
        points+=1
        check(message)
        chat_id = message.chat.id
        photo = open(r"Снимок экрана 2024-07-12 145859.png", 'rb')
        bot.send_photo(chat_id, photo=photo)
        stats_pet(message)

    elif message.text == 'Тренировка':
        satiety-=35
        happiness+=10
        energy-=20
        points+=3
        money+=5
        check(message)
        stats_pet(message)

    elif message.text == 'Прогулка':
        satiety-=15
        happiness+=35
        energy-=10
        points+=2
        check(message)
        stats_pet(message)


@bot.message_handler(content_types=['text'])
def bot1_message(message):
    global money, name
    if message.text == 'Информация о питомце':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='Данные питомца')
        item2 = types.KeyboardButton(text='Карточка питомца')
        item3 = types.KeyboardButton(text='В главное меню')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Данные питомца':
        chat_id = message.chat.id
        photo = open(r"Снимок экрана 2024-07-12 145822.png", 'rb')
        bot.send_photo(chat_id, photo=photo)
        stats_pet(message)

    elif message.text == 'Карточка питомца':
        chat_id = message.chat.id
        photo = open(r"Снимок экрана 2024-07-12 145822.png", 'rb')
        bot.send_photo(chat_id, photo=photo)
        bot.send_message(message.chat.id, f'Вашего питомца зовут {name}')

    elif message.text == 'В главное меню':
        markup = ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = KeyboardButton(text='Еда')
        button2 = KeyboardButton(text='Сон')
        button3 = KeyboardButton(text='Прогулка')
        button4 = KeyboardButton(text='Тренировка')
        button5 = KeyboardButton(text='Информация о питомце')
        button6 = KeyboardButton(text='Игры с монетами')
        button7 = KeyboardButton(text='Уровень питомца')
        button8 = KeyboardButton(text='Поинты')
        button9 = KeyboardButton(text='Магазин')
        markup.add(button1, button2, button3, button4, button5, button6, button7, button8, button9)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Уровень питомца':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='info о получении уровней')
        item2 = KeyboardButton(text='info о получении поинтов')
        item3 = types.KeyboardButton(text='В главное меню')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'info о получении уровней':
        bot.send_message(message.chat.id, f'Уровень персонажа повышается на 1 каждые 50 заработанных поинтов! Чем больше уровень - тем больше монет вы получаете!Ваш уровень - {lvl}')

    elif message.text == 'info о получении поинтов':
        bot.send_message(message.chat.id, f'При получении поинтов вы прокачиваете свой уровень. Вы получаете определенное кол-во поинтов за каждую активность в игре. Кол-во поинтов у вас - {points}')

    elif message.text == 'Магазин':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = KeyboardButton(text='Стикеры')
        item2 = types.KeyboardButton(text='В главное меню')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Купить стикеры_1':
        if money < 50:
            bot.send_message(message.chat.id, 'Вам не хватает монет!')
        else:
            bot.send_message(message.chat.id, 'https://t.me/addstickers/OwlsBotPlay')

    elif message.text == 'Стикеры':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='Стикеры_1')
        item2 = KeyboardButton(text='Стикеры_2')
        markup.add(item1, item2)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Стикеры_1':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='Купить стикеры_1')
        item2 = KeyboardButton(text='В главное меню')
        item3 = KeyboardButton(text='Info')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Info':
        chat_id = message.chat.id
        photo_1 = open(r"Снимок экрана 2024-07-12 190916.png", 'rb')
        photo = open(r"Снимок экрана 2024-07-12 200245.png", 'rb')
        bot.send_photo(chat_id, photo=photo_1)
        bot.send_photo(chat_id, photo=photo)
        bot.send_message(message.chat.id, 'Вы можете ознакомиться со стикерпаками!')

    elif message.text == 'Стикеры_2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton(text='Купить стикеры_2')
        item2 = KeyboardButton(text='В главное меню')
        item3 = KeyboardButton(text='Info')
        markup.add(item1, item2, item3)
        bot.send_message(message.chat.id, 'Выберите вариант:', reply_markup=markup)

    elif message.text == 'Купить стикеры_2':
        if money < 50:
            bot.send_message(message.chat.id, 'Вам не хватает монет!')
        else:
            bot.send_message(message.chat.id, 'https://t.me/addstickers/Sova_Sofa')

bot.polling( )