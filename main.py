import random
from urllib.request import urlopen
from texts import *

import telebot
from telebot import types
import config

token = '6753721531:AAETHzEKAks5ipnd9jVjVBVwm2riqbR_MqY'
bot = telebot.TeleBot(token)

# money = 5000
global money
global home_imp_city
global benirus_home
global bandit
global service



@bot.message_handler(commands=['xxx'])
def an_mes(message):
    bot.send_message(message.chat.id, "Второй пошёл!")

@bot.message_handler(commands=['ccc'])
def an_mes(message):
    name1 = message.from_user.first_name
    if name1[-1] == 'й' or 'я':
        name = f'{message.from_user.first_name[:-1][:-1]}юшка'
    elif name1[-1] == 'а':
        name = f'{message.from_user.first_name[:-1]}ушка'
    else:
        name = f'{message.from_user.first_name}ушка'

    # bot.send_message(message.chat.id, f"Я знаю ваше имя! Ваше имя - {message.from_user.first_name}")
    bot.send_message(message.chat.id, f"Я знаю ваше имя! Ваше имя - {name}")

@bot.message_handler(commands=['start'])
def an_mes(message):

    # Формирование приветствия
    name1 = message.from_user.first_name
    if name1[-1] == 'й' or 'я':
        name = f'{message.from_user.first_name[:-1][:-1]}юшка'
    elif name1[-1] == 'а':
        name = f'{message.from_user.first_name[:-1]}ушка'
    else:
        name = f'{message.from_user.first_name}ушка'

    bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/тамриэль.jpg', 'rb'))
    global money
    global home_imp_city
    global bandit
    global benirus_home
    global service

    bandit = False
    home_imp_city = False
    benirus_home = False
    money = 5000
    service = False

    # markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup = types.ReplyKeyboardMarkup()
    btn1 = types.KeyboardButton('Отправиться в Имперский город')
    btn2 = types.KeyboardButton('Отправиться в Скайрим')
    btn3 = types.KeyboardButton('Остаться в Анвиле')
    btn4 = types.KeyboardButton('Отправиться с отрядом наёмников в Чернотопье')
    btn5 = types.KeyboardButton('Посчитать деньги')
    markup.add(btn1, btn2, btn3, btn4, btn5)
    bot.send_message(message.chat.id, text=f"Привет, {name}\nВас приветствует бот, который\nпоможет вам путешествовать "
                                           f"по Тамриэлю.\nУ вас в мошне 5000 золотых. Куда вы отправитесь в первую "
                                           f"очередь? Не забывайте, что "
                                           f"для путешествия вам необходимы деньги. Расценки следующие: до Имперского "
                                           f"города - 40 золотых, до Скайрима - 50. В отряд до Чернотопья вас "
                                           f"возьмут бесплатно", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def func(message):
    global money
    global home_imp_city
    global service

    def money_num(message):
        global money
        bot.send_message(message.chat.id, text=f'Сейчас в вашей мошне {money} золотых')

    if (message.text == 'Посчитать деньги'):
        money_num(message)

    def no_monew():
        global money
        # if money < 0:
        bot.send_message(message.chat.id, text='О нет! Похоже у вас совсем не осталось денег! Вас тут же бросают в '
                                               'тюрьму за долги, где вы и кончаете свои дни')
        bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/тюрьма.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Закончить игру')
        btn2 = types.KeyboardButton('/start')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)


    if(message.text == "Отправиться в Имперский город" or message.text =='Вернуться в город' or
    message.text == 'Нет, следует покинуть это место'):

        global home_imp_city
        global money
        if money <0:
            no_monew()
        else:

            ### Проверка наличия дома в Имперском городе
            if home_imp_city == False:
                money = money - 40
            if home_imp_city == True:
                money = money - 15

            bot.send_message(message.chat.id, text="Вы прибыли в Имперский город. Куда вы отправитесь теперь?")
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/impcity.jpg', 'rb'))

            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Вернуться обратно в Анвил')
            btn2 = types.KeyboardButton('Отправиться на Арену')
            # btn3 = types.KeyboardButton('Пойти в Торговый район')
            btn4 = types.KeyboardButton('Пойти в Портовый район')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
            markup.add(btn1, btn2,  btn4, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if money < 0:
        no_monew()
    else:
        if (message.text == "Отправиться в Скайрим" or message.text == 'Выйти в Фолкрит'):

            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/folkrith.jpg', 'rb'))
            bot.send_message(message.chat.id, text="Вы прибыли в Фолккрит, лежащий сразу за Белым проходом. Что вы предпримете дальше?")

            # global money
            money = money - 50

            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Пойти в дом ярла')
            btn2 = types.KeyboardButton('Посетить таверну')
            btn3 = types.KeyboardButton('Вернуться обратно в Анвил')

            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
            markup.add(btn1, btn2, btn3, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)



# Третий вариант
#     if money < 0:
#         no_monew()
#     else:

        if (message.text == "Остаться в Анвиле" or message.text == "Вернуться обратно в Анвил" or message.text ==
                "Вернуться в Анвил"):
            # no_monew()
            if money < 0:
                no_monew()
            else:
                bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/anvil.jpg', 'rb'))
                bot.send_message(message.chat.id, text="Вы Анвиле. Что делать в этом прекрасном городе?\n"
                                                       "Здесь вы можете купить отличный особняк по низкой цене\n"
                                                       "можно попробовать устроиться смотрителем в местный маяк или служить "
                                                       "здесь в замковой страже. А может, этот город слишком тихий и пора в Имперский город?")

                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('Поскорее купить особняк!')
                btn2 = types.KeyboardButton('Устроиться смотрителем маяка')
                btn3 = types.KeyboardButton('Отправиться в Имперский город')
                btn4 = types.KeyboardButton('Отправиться служить в замок стражником')
                btn5 = types.KeyboardButton('Посчитать деньги')
                btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
                bot.send_message(message.chat.id,
                                 text="Ваши действия... ", reply_markup=markup)


# Четвёртый вариант

    if (message.text == 'Отправиться с отрядом наёмников в Чернотопье'):
        # no_monew()
        if money < 0:
            no_monew()
        else:
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/отряд.png', 'rb'))
            bot.send_message(message.chat.id, text="Вы рискнули и пошли в Чернотопье. Не лучшее место для человека."
                                                   " Но вот спустя несколько дней вы прибыли, где-то около болота построили "
                                                   "лагерь. Командир набирает добровольцев, чтобы отправиться в разведку к "
                                                   "огромному Древу Ящера. Что скажете?")


            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Я для этого и пришёл сюда! \nМоё первое задание! Наконец-то!')
            btn2 = types.KeyboardButton('Лучше останусь в лагере \nследить за костром и \nпатрулировать частокол')
            btn3 = types.KeyboardButton('О Девять! Тут так душно!\n Зачем я сюда пошёл? \nПопытаться дать взятку командиру \nи '
                                        'попросить отправить меня \nвербовать новых воинов')
            btn4 = types.KeyboardButton('Сегодня моя очередь отдыхать. \nЗадания - завтра')
            btn5 = types.KeyboardButton('Посчитать деньги')
            markup.add(btn1, btn2, btn3, btn4, btn5)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)




    # обработка Имперского города
    # Арена

    if (message.text == 'Отправиться на Арену'):
        # no_monew()
        if money < 0:
            no_monew()
        else:
            bot.send_message(message.chat.id, text='Вы прибыли на Арену. Хотите ли поучаствовать в сражениях или просто '
                                                   'сделать ставку? Не забывайте, что на Арене вы проведёте целый день, а '
                                                   'за пребывание в городе надо платить по 40 золотых в день.')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Нет, следует покинуть это место')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')

            markup.add(btn1, btn2, btn3, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/арена.jpg', 'rb'))

    def lost(message):
        # no_monew()
        global money
        if money <0:
            no_monew()
        else:
            bot.send_message(message.chat.id, text='Увы, вы приграли! Ну, что теперь?')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')

            markup.add(btn1, btn2, btn3, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
    def buy_benirus_home(message):
        global money

        money = money - 5000
        # no_monew()
        bot.send_message(message.chat.id, text='Поздравляем! Вы купили дом в Анвиле! Если хотите, можете его '
                                               'отремонтировать, так как он в ужасном состоянии. Потому и стоит так'
                                               ' дешево')
        bot.send_photo(message.chat.id,
                       open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/разруха бенируса.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup()
        # btn1 = types.KeyboardButton('Переночевать в доме')
        btn2 = types.KeyboardButton('Вернуться в Анвил')
        btn3 = types.KeyboardButton('Затеять ремонт')
        btn5 = types.KeyboardButton('Посчитать деньги')
        btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')

        markup.add(btn2, btn3, btn5, btn6)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)


    if (message.text == 'Сделать ставку'):
        money = money - 100
        if money <0:
            no_monew()
        else:


            bot.send_message(message.chat.id, text='Выберите, на кого вы хотите поставить. Ставка составляет 100 золотых')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Мощный аргонианин (Вероятность победы 75%)')
            btn2 = types.KeyboardButton('Плотный эльф (вероятность 50%)')
            btn3 = types.KeyboardButton('Новичок из Скайрима (10%)')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
            # bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/арена.jpg', 'rb'))

    if (message.text == 'Мощный аргонианин (Вероятность победы 75%)'):

        vic = random.choice([1, 2, 3, 4])
        print(vic)
        if vic == 1 or vic ==2 or vic ==3:
            bot.send_message(message.chat.id, text='Ну конечно. Аргонианин выиграл и немного вас обогатил. '
                                                   'Вы возвращаете свою ставку и ещё 25 золотых. Что дальше?')
            # global money
            money = money + 125
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        else:
            lost(message)

    if (message.text == 'Плотный эльф (вероятность 50%)'):
        vic = random.choice([1, 2, 3, 4])
        if vic == 1 or vic == 2:
            # global money
            money = money + 50
            bot.send_message(message.chat.id, text='Неплохо. Шансы были немалые, и вы немного обогатились. Получите в '
                                                   'кассе 150 золотых')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        else:
            lost(message)

    if (message.text == 'Новичок из Скайрима (10%)'):
        vic = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        if vic == 1 :
            # global money
            money = money + 1100
            print(vic)
            bot.send_message(message.chat.id, text='Отлично! Риск был велик, но он оправдался! Вы не только вернули '
                                                   'ставку, но и получили 1000 золотых сверху!Чем займётесь дальше?')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        else:
            lost(message)

    if (message.text == 'Пойти сражаться'):
        bot.send_message(message.chat.id, text = 'Вы очень рискуете! Но если вы действительно готовы, выберите соперника'
                                                 ' (в скобках ваша вероятность на победу и возможный выигрыш. Так что крепко подумайте, '
                                                 'прежде чем рисковать жизнью)')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Опытный аргонианин (25%, 2000)')
        btn2 = types.KeyboardButton('Сильный эльф (50%, 800')
        btn3 = types.KeyboardButton('Молодой норд (90%, 100)')
        btn4 = types.KeyboardButton('Вернуться в город')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    def lost_fight(message):
        bot.send_message(message.chat.id, text='Увы, несмотря на все ваши усилия, вы геройски погибли на Арене. Ваш путь окончен')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Путешествие закончено')

        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)






    def semi_lost(message):
        global money
        bot.send_message(message.chat.id, text='Вы получили тяжкое ранение. Вы тратите 500 золотых на лечение.')
        money = money - 500
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Вернуться в город')

        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    def deth(message):
        bot.send_message(message.chat.id, text='Вы окончили свой славный путь. Может, кто-то вспомнит о вас и '
                                               'сочинит песенку, а может и безвестная могилка ничего не скажет '
                                               'проходящему путнику. Суров путь искателя приключений',
                         reply_markup=types.ReplyKeyboardRemove())
        bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/кладбище.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Закончить игру')
        btn2 = types.KeyboardButton('/start')
        markup.add(btn1, btn2)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    def vic_arena_img(message):
        pass

        ########### СКАЙРИМ

    if (message.text == "Пойти в дом ярла"):
        if money <0:
            no_monew()
        else:
        # no_monew()
            bot.send_message(message.chat.id,
                             text="Ярл смотрит на вас с недоумением. Единственное, что он может предложить, сразиться ради "
                                  "его развлечения с крепким нордом из его стражи. Только будьте осторожны!")
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Вернуться обратно в Анвил')
            btn2 = types.KeyboardButton('Отправиться в Имперский город')
            btn4 = types.KeyboardButton('Сразиться с нордом!')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
            markup.add(btn1, btn2, btn4, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Сразиться с нордом!'):
        if money <0:
            no_monew()
        else:
        # no_monew()
            vic = random.choice([1, 2])
            print(vic)
            if vic == 1:
                bot.send_message(message.chat.id,
                                 text="Вы яростно сражались, но, похоже, ваше путешествие в Скайрим было ошибкой. Вы нашли "
                                      "гибель в этом холодном и неприветливом краю")
                deth(message)

            if vic == 2:
                bot.send_message(message.chat.id,
                                 text="Вы яростно сражались и одолели крепкого норда! Ярл повеселился, и вы получили 500 "
                                      "золотых! Но скоро ярл протрезвеет и поймёт, что лишился лучшего воина. И вы, как "
                                      "разумный человек, понимаете, что лучше уходить")
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('Вернуться обратно в Анвил')
                btn2 = types.KeyboardButton('Отправиться в Имперский город')
                btn5 = types.KeyboardButton('Посчитать деньги')
                btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
                markup.add(btn1, btn2, btn5, btn6)
                bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if (message.text == "Посетить таверну"):
        # no_monew()

        if money <0:
            no_monew()
        else:
            bot.send_message(message.chat.id,
                             text="Кругом пьяные норды")
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Напиться вдрызг с этими весёлыми ребятами!')
            btn2 = types.KeyboardButton('Отправиться в Имперский город')
            # btn4 = types.KeyboardButton('Сразиться с нордом!')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
            markup.add(btn1, btn2, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if (message.text == "Напиться вдрызг с этими весёлыми ребятами!"):
        # no_monew()
        if money <0:
            no_monew()
        else:
            vic = random.choice([1, 2, 3])
            if vic == 1:
                bot.send_message(message.chat.id,
                                 text="Похоже, вы напились, началась драка, и ничем хорошим она не закончилась")
                deth(message)

            if vic == 2:
                bot.send_message(message.chat.id,
                                 text="Похоже, ваш собутыльник оказался крупной шишкой! Оставшись довольным, он просто так "
                                      "подарил вам 500 золотых. Пора убираться из города, пока он не протрезвел и не осознал "
                                      "свою ошибку")
                money += 500
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('Вернуться в Анвил')
                btn2 = types.KeyboardButton('Отправиться в Имперский город')
                btn4 = types.KeyboardButton('Выйти в Фолкрит')
                btn5 = types.KeyboardButton('Посчитать деньги')
                btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
                markup.add(btn1, btn2, btn4, btn5, btn6)
                bot.send_message(message.chat.id,
                                 text="Ваши действия... ", reply_markup=markup)
            if vic == 3:
                bot.send_message(message.chat.id,
                                 text="Похоже, вы пропили 300 талантов. Погуляли славно, но пора и честь знать")
                money -= 300
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('Вернуться в Анвил')
                btn2 = types.KeyboardButton('Отправиться в Имперский город')
                btn4 = types.KeyboardButton('Выйти в Фолкрит')
                btn5 = types.KeyboardButton('Посчитать деньги')
                btn6 = types.KeyboardButton('Купить номер "Вороного курьера"')
                markup.add(btn1, btn2, btn4, btn5, btn6)
                bot.send_message(message.chat.id,
                                 text="Ваши действия... ", reply_markup=markup)


    if (message.text == 'Опытный аргонианин (25%, 2000)'):
        # no_monew()

        if money <0:
            no_monew()
        else:
            vic = random.choice([1, 2, 3, 4])
            print(vic)
            if vic == 1:
                # global money
                money = money + 2000
                bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/arena_win.jpg', 'rb'))
                bot.send_message(message.chat.id, text='Поздравляем!Вы не только вы не только выжили, но и выиграли 2000 золотых. '
                                 'Потратьте их с умом. Однако, чем займётесь дальше?')
                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('Сделать ставку')
                btn2 = types.KeyboardButton('Пойти сражаться')
                btn3 = types.KeyboardButton('Вернуться в город')

                markup.add(btn1, btn2, btn3)
                bot.send_message(message.chat.id,
                                 text="Ваши действия... ", reply_markup=markup)
            elif vic == 2:
                semi_lost(message)
                print('Ранение')
            else:
                lost_fight(message)

    if (message.text == 'Сильный эльф (50%, 800'):
        vic = random.choice([1, 2, 3, 4])
        if vic == 1 or vic == 2:
            # global money
            money = money + 800
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/arena_win.jpg', 'rb'))
            # audio = open(r'C:/PythonFiles/Telegram_traveller_Bot/audio/аплодисменты.mp3', 'rb')
            # bot.send_audio(message.chat.id, audio)
            # audio.close()
            bot.send_message(message.chat.id, text='Поздравляем!Вы вы выжили и выиграли 800 золотых. '
                             'Потратьте их с умом. Однако, чем займётесь дальше?')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        elif vic == 3:
            semi_lost(message)
            print('Ранение')
        else:
            lost_fight(message)

    if (message.text == 'Молодой норд (90%, 100)'):
        vic = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
        if vic != 1 and vic != 2:
            # global money
            money = money + 100
            bot.send_message(message.chat.id, text='Ну конечно, у вас были хорошие шансы. Норд отдал свою жизнь за '
                                                   '100 золотых')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Сделать ставку')
            btn2 = types.KeyboardButton('Пойти сражаться')
            btn3 = types.KeyboardButton('Вернуться в город')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        elif vic == 2:
            semi_lost(message)
            print('Ранение')
        else:
            lost_fight(message)

    if (message.text == 'Путешествие закончено'):
        deth(message)


################## Портовый район
    if (message.text == 'Пойти в Портовый район' or message.text == 'Вернуться в Портовый район' or message.text ==
            'Уйти прочь'):
        # no_monew()
        if money <0:
            no_monew()
        else:
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/портовый район.jpg', 'rb'))
            bot.send_message(message.chat.id, text='Вы прибыли в Портовый район. Чем займётусь тут? Здесь можно немного '
                                                   'порыбачить. Это безопасно, но много денег не принесёт. Можно '
                                                   'договориться со стражей и поохотиться на грязевых крабов. Это более '
                                                   'прибыльно, но немного рискованно. А ещё можно купить здесь небольшой '
                                                   'домик. Это позволит вам тратиь не по 40 золотых на приезд в город и проживание в нём, а всего 15.'
                                                   'Также вы можете поговорить с одним типом. Он говорит, что может '
                                                   'помочь заработать')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Пойти порыбачить')
            btn2 = types.KeyboardButton('Поохотиться на крабов')
            btn3 = types.KeyboardButton('Купить дом за 2000 золотых')
            btn4 = types.KeyboardButton('Поговорить со странным типом')
            btn5 = types.KeyboardButton('Посчитать деньги')
            btn6 = types.KeyboardButton('Вернуться в город')
            btn7 = types.KeyboardButton('Купить номер "Вороного курьера"')
            global bandit
            if bandit == False:
                markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            if bandit == True:
                markup.add(btn1, btn2, btn3, btn5, btn6)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Пойти порыбачить'):
        # no_monew()
        if money <0:
            no_monew()
        else:
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/рыбалка.jpg', 'rb'))
            bot.send_message(message.chat.id, text = 'Итак, ловите удачу, а заодно деньги. ')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Начать рыбалку')
            btn2 = types.KeyboardButton('Посчитать деньги')
            btn3 = types.KeyboardButton('Вернуться в Портовый район')


            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Начать рыбалку'):
        vic = random.choice([1, 2, 3, 4])
        if vic == 1:
            bot.send_message(message.chat.id, text='Вам повезло. Ваш улов на сегодня потянет на 30 золотых!')
            money = money + 30
        elif vic == 2:
            bot.send_message(message.chat.id, text='Неплохо. На 15 золотых потянет')
            money = money + 15
        else:
            bot.send_message(message.chat.id, text='Что-то не ловится рыбка, ни большая, ни маленькая')

        bot.send_message(message.chat.id, text='Итак, ловите удачу, а заодно деньги. ')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Начать рыбалку')
        btn2 = types.KeyboardButton('Посчитать деньги')
        btn3 = types.KeyboardButton('Вернуться в Портовый район')
        btn4 = types.KeyboardButton('Вернуться в город')

        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Купить дом за 2000 золотых'):
        # global home_imp_city
        if home_imp_city == False and money >= 2000:
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/дом в ИГ.jpg', 'rb'))
            bot.send_message(message.chat.id, text='Вот такой дом предлагается к продаже. Он маленький, простенький, '
                                                   'но зато недорогой. И позволяет экономить при проживании в Имперском '
                                                   'городе.')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Купить дом')
            btn2 = types.KeyboardButton('Посчитать деньги')
            btn3 = types.KeyboardButton('Вернуться в Портовый район')

            markup.add(btn1, btn2, btn3)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)
        if home_imp_city == True:
            bot.send_message(message.chat.id, text='Вы уже купили этот дом!')

        if home_imp_city == False and money < 2000:
            bot.send_message(message.chat.id, text='У вас недостаточно денег')

    if (message.text == 'Купить дом'):
        # global home_imp_city
        if home_imp_city == True:
            bot.send_message(message.chat.id, text='Вы уже купили этот дом!')
            return 0
        elif home_imp_city == False and money < 2000:
            bot.send_message(message.chat.id, text='У вас недостаточно денег')
            return 0
        home_imp_city = True

        bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/дом ИГ внутри.jpg', 'rb'))
        money = money - 2000
        bot.send_message(message.chat.id, text='Поздравляем, вы купили недвижимость в столице!')

    if (message.text == 'Поохотиться на крабов'):
        # no_monew()
        bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/грязевой.jpg', 'rb'))
        bot.send_message(message.chat.id, text='Пробуйте охотитьмя на крабов. Только помните, они довольно опасны!')

        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Начать охоту')
        btn2 = types.KeyboardButton('Посчитать деньги')
        btn3 = types.KeyboardButton('Вернуться в Портовый район')

        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Начать охоту'):
        vic = random.choice([1, 2, 3, 4])
        print(vic)
        if vic == 1:
            bot.send_message(message.chat.id, text='Поздравляем с удачной охотой! Стражники выплатили вам 40 золотых!')
            money += 40
        elif vic == 2 :
            bot.send_message(message.chat.id, text='Неплохой улов! Стражники выплатили вам 20 золотых!')
            money += 20
        elif vic == 3:
            if money >= 50:
                money -= 50
                bot.send_message(message.chat.id,
                                 text='Увы, краб ранил вас и ушёл. Придётся заплатить 50 золотых за лечение')
            if money < 50:
                bot.send_message(message.chat.id,
                                 text='Увы, краб ранил вас и ушёл. А у вас даже нет денег заплатить за лечение. Рана '
                                      'начала гноиться, и через несколько часов вы умираете')
                deth(message)
        else:
            bot.send_message(message.chat.id,
                             text='Охота не принесла результатов. Ну, хотя бы невредимым вернулись.')

    if (message.text == 'Поговорить со странным типом'):
        print(bandit)
        bot.send_message(message.chat.id, text='Странный тип говорит вам, что в город едет обоз торговца из Скинграда. '
                                               'Сам торговец - дерьмовый человек. Так что можно его ограбить. Конечно, '
                                               'есть риск быть пойманным или даже убитым, но дело стоит того. Вы в игре?')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Ввязаться в эту интригу')
        btn2 = types.KeyboardButton('Отказаться')
        btn3 = types.KeyboardButton('Сдать проходимца страже')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Отказаться'):
        bot.send_message(message.chat.id, text='Тип усмехнулся, поссчитав вас трусом')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Уйти прочь')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)




    if (message.text == 'Сдать проходимца страже'):
        bandit = True
        bot.send_message(message.chat.id, text='Вы получили от стражи премию 100 золотых')
        money+=100
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Вернуться в Портовый район')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Ввязаться в эту интригу'):
        # bandit = True
        bot.send_message(message.chat.id, text='Тёмной ночью вы переправились через бухту. Долго ждать не пришлось: '
                                               'вскоре появился обоз. Пора действовать!')
        vic = random.choice([1, 2, 3, 4, 5])
        print(vic)
        if vic == 1:
            money += 2000
            # global bandit
            bandit = True
            bot.send_message(message.chat.id,
                             text='Кажется, всё прошло удачно! Вы прирезали пару стражников - кровь на руках - мелочь -'
                                  'и добыча вышла по 2000 золотых каждому! Иногда полезно кого-нибудь убить.')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Вернуться в Портовый район')
            markup.add(btn1)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

        if vic == 2 or vic == 5:
            # global bandit
            bandit = True
            bot.send_message(message.chat.id,
                             text='Сначала всё шло хорошо, но потом стражники убили вашего напарника, и вы поняли, что '
                                  'пора делать ноги. Повезло, что вернулись домой невредимым.')
            markup = types.ReplyKeyboardMarkup()
            btn1 = types.KeyboardButton('Вернуться в Портовый район')
            markup.add(btn1)
            bot.send_message(message.chat.id,
                             text="Ваши действия... ", reply_markup=markup)

        if vic == 3:
            # global bandit
            bandit = False
            bot.send_message(message.chat.id,
                             text='Куда же вы полезли? Понятно, что обоз охраняют профессиональные воины. Вы пали в бою.')
            types.ReplyKeyboardRemove()
            deth(message)
            # lost_fight(message)
            
        if vic == 4:

            bandit = False
            bot.send_message(message.chat.id,
                             text='Куда же вы полезли? Понятно, что обоз охраняют профессиональные воины. Вас схватили'
                                  ' и отвезли в Имперский город, судили и казнили.')

            types.ReplyKeyboardRemove()
            deth(message)

    ###################### АНВИЛ

    def return_to_anvil():
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Вернуться в Анвил')
        markup.add(btn1)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text) == 'Поскорее купить особняк!':
        if benirus_home == False:
            # no_monew()
            if money < 5000:
                print('Мало денег')
                bot.send_message(message.chat.id, text= 'У вас недостаточно денег. Но посмотреть можете')
                bot.send_photo(message.chat.id,
                               open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/дом бенируса.jpg', 'rb'))

            return_to_anvil()

            if money >= 5000:
                print('Достаточно денег')
                bot.send_message(message.chat.id, text='Вот так выглядит особняк снаружи. Хотите ли посмотреть изнутри')
                bot.send_photo(message.chat.id,
                               open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/дом бенируса.jpg', 'rb'))

                markup = types.ReplyKeyboardMarkup()
                btn1 = types.KeyboardButton('По такой цене? Беру не глядя!')
                btn2 = types.KeyboardButton('Ну, давайте осмотрим')
                btn3 = types.KeyboardButton('Вернуться в Анвил')
                btn4 = types.KeyboardButton('Посчитать деньги')
                markup.add(btn1, btn2, btn3, btn4)
                bot.send_message(message.chat.id,
                                     text="Ваши действия... ", reply_markup=markup)
        if benirus_home == True:
            bot.send_message(message.chat.id, text='Вы уже купили этот дом!')
            return_to_anvil()


    if (message.text == 'По такой цене? Беру не глядя!' or message.text == 'Купить особняк'):
        buy_benirus_home(message)

    if (message.text == 'Ну, давайте осмотрим'):
        bot.send_message(message.chat.id, text='Дом явно нужно '
                                               'отремонтировать, так как он в ужасном состоянии. Потому и стоит так'
                                               ' дешево. Стоит ли тратиться на него?')
        bot.send_photo(message.chat.id,
                       open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/разруха бенируса.jpg', 'rb'))
        markup = types.ReplyKeyboardMarkup()

        btn2 = types.KeyboardButton('Вернуться в Анвил')
        btn3 = types.KeyboardButton('Купить особняк')
        btn5 = types.KeyboardButton('Посчитать деньги')

        markup.add(btn2, btn3, btn5)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Затеять ремонт'):
        if money < 3000:
            bot.send_message(message.chat.id, text='У вас недостаточно денег!')
            return_to_anvil()
        if money >= 3000:
            money -= 3000
            bot.send_message(message.chat.id, text='Теперь у вас дома прекрасная обстановка!')
            bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/после ремонта.jpg', 'rb'))
            return_to_anvil()

    if (message.text == 'Купить номер "Вороного курьера"'):

        money -= 10
        # no_monew()
        if money <0:
            no_monew()
        else:
            text = news()
            bot.send_message(message.chat.id, text='Вы потратили 10 золотых на газету')
            bot.send_message(message.chat.id, text=text)

    if (message.text == 'Отправиться служить в замок стражником'):
        bot.send_message(message.chat.id, text='Вы приняты в стражники замка. У вас есть два варианта. Спокойно '
                                               'прослужить полгода и получить 500 золотых или отправиться на рискованное '
                                               'задание в Золотую бухт у и получить две тысячи в течение недели.')
        markup = types.ReplyKeyboardMarkup()
        btn1 = types.KeyboardButton('Спокойно прослужить полгода')
        btn2 = types.KeyboardButton('Конечно, рискнуть!')
        btn3 = types.KeyboardButton('Вернуться в Анвил')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Спокойно прослужить полгода'):
        if service == False:
            money += 500
            service = True
            bot.send_message(message.chat.id, text='Вы прослужили полгода в замке Анвила. Это было невесело, тоскливо, как в '
                                                   'тюрьме. Но, в отличие от тюрьмы, вы получили обещанные 500 золотых')
            return_to_anvil()
        if service == True:
            bot.send_message(message.chat.id, text='Сейчас стражники не требуются в замке Анвила')
            return_to_anvil()

    if (message.text == 'Устроиться смотрителем маяка'):
        bot.send_message(message.chat.id,
                         text='Иногда тут бывает вакансия: мало кому охота целыми днями - особенно ночами - сидеть в '
                              'одном и том же месте. Хотя пейзажи здесь действительно великолепные, да ещё и деньги за '
                              'это платят')
        bot.send_photo(message.chat.id, open('C:/PythonFiles/Telegram_traveller_Bot/venv/img/маяк анвила.jpg', 'rb'))
        try_vac = random.choice([0, 1, 2, 3, 4, 5, 6, 7])
        if try_vac == 7:
            bot.send_message(message.chat.id, text='Вам повезло. Вы поработали недельку в маяке, получили 50 золотых.'
                                                   'Когда снова появится такая возможность - неизвестно.')
            return_to_anvil()
        if try_vac != 7:
            bot.send_message(message.chat.id, text='В настоящее время смотритель на маяке не требуется. '
                                                   'Попробуйте как-нибудть в другой раз')
            return_to_anvil()

    if (message.text == 'Конечно, рискнуть!'):
        bot.send_message(message.chat.id, text='Стража города отправляется на операцию по ликвидации нескольких '
                                               'бандитских лагерей к северу от Золотой дороги. Дело может быть выгодным, '
                                               'но рискованным. Согласитесь ли вы на этот риск?')
        markup = types.ReplyKeyboardMarkup()
        btn2 = types.KeyboardButton('Безусловно! В Обливион разбойников!')
        btn3 = types.KeyboardButton('Вернуться в Анвил')
        markup.add( btn2, btn3)
        bot.send_message(message.chat.id,
                         text="Ваши действия... ", reply_markup=markup)

    if (message.text == 'Безусловно! В Обливион разбойников!'):
        bot.send_message(message.chat.id, text='Вы отправились вместе со стражниками на охоту на разбойников!')
        vic = random.choice([1, 2, 3, 4, 5, 6, 7])
        if vic == 1:
            bot.send_message(message.chat.id, text='Кажется, разбойники оказались хитрее и сильнее, чем вы думали. '
                                                   'Вы пали в бою')
            deth(message)
        if vic == 2 or vic == 3 or vic ==4:
            money -= 100
            bot.send_message(message.chat.id, text='Ну что ж, вы рискнули, но риск не совсемоправдался. Разбойники '
                                                   'побеждены, вы получили награду в 200 золотых. Но на лечение ран '
                                                   'ушло 300 золотых. Так что вы в убытке.')
            return_to_anvil()
        if vic == 5:
            bot.send_message(message.chat.id, text='Охота прошла довольно успешно. Вы разбили один лагерь, но наделали '
                                                   'слишком много шума и остальные ушли. Так что ваша награда всего 100 золотых. ')
            return_to_anvil()

        if vic == 6:
            money += 500
            bot.send_message(message.chat.id, text='Вы оказались отличным воином! Все разбойники разбиты, предводитель'
                                                   ' стражников в восторге! Вам выплатили 500 золотых. Жаль, что '
                                                   'бандиты северных лагерей прознали про вас и скрылись.')
            return_to_anvil()

        if vic == 7:
            money += 2000
            bot.send_message(message.chat.id, text='Вы оказались отличным воином! Все разбойники разбиты, предводитель'
                                                   ' стражников в восторге! Вам выплатили 1500 золотых, а капитан стражи '
                                                   'ещё добавил 500 премии!')
            return_to_anvil()









bot.infinity_polling()
