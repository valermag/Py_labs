from logging import StringTemplateStyle
import telebot
import os

import random
 
from telebot import types

class Place(object):   
    emp_count = 0  
  
    def __init__(self, adres, square, price, number_own,picture):  
        self.adres = adres  
        self.square = square
        self.price = price
        self.number_own = number_own 
        self.picture = os.system(f"{picture}")

        Place.emp_count += 1  
  
    def display_count(self):  
        print('Всего сотрудников: %d' % Place.empCount)  
    def get_square(self):
        return self.square
  
    def display_place(self):  
        return f'Адрес: {self.adres}.\n Площадь: {self.square} метров квадратных. \n Цена за месяц: {self.price}. \n Номер арендадателя: {self.number_own}.\n {self.picture}'
place1=Place("ул.Голубева 12",'140','550$','+375445567890','E:\bot_curs\1.jpg')
place2=Place("ул.Ольшевского 51",'100','480$','+375447565690','E:\bot_curs\1.jpg')
place3=Place("ул.Тараканова 4А",'89','300$','+375290986745','E:\bot_curs\1.jpg')
place4=Place("пр.Дзержинского 15",'70','250$','+375293476745','E:\bot_curs\1.jpg')
place5=Place("пр.Правды 7",'110','430$','+375290980005','E:\bot_curs\1.jpg')

mas = [place1,place2,place3,place4,place5]


#-----------------------------------------------------------------------------------------------------------      
 #BOT
bot = telebot.TeleBot('1715199163:AAG_nJC8vpbL1ignSxUL8oZ-kHxhbaVCffA')


@bot.message_handler(commands=['start'])
def welcome(message):
 
    # keyboard
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Все варианты")
    item2 = types.KeyboardButton("По площади")
 
    markup.add(item1, item2)
 
    bot.send_message(message.chat.id, "Добро пожаловать, {0.first_name}!\nЯ - <b>{1.first_name}</b>, бот созданный чтобы помочь тебе найти варианты аренды площади".format(message.from_user, bot.get_me()),
        parse_mode='html', reply_markup=markup)
 
@bot.message_handler(content_types=['text'])
def lalala(message):
    if message.chat.type == 'private':
        if message.text == 'Все варианты':
            for i in range(0,len(mas)):
                p = mas[i].display_place()
                bot.send_message(message.chat.id, f" {p}")
        elif message.text == 'По площади':
 
            markup = types.InlineKeyboardMarkup(row_width=2)
            item1 = types.InlineKeyboardButton(">=100", callback_data='good')
            item2 = types.InlineKeyboardButton("<100", callback_data='bad')
 
            markup.add(item1, item2)
 
            bot.send_message(message.chat.id, 'какая площадь вас интересует?(в м^2)', reply_markup=markup)
        else:
            bot.send_message(message.chat.id, 'Я не знаю что ответить 😢')
 
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    try:
        if call.message:
            if call.data == 'good':
                count=0
                bot.send_message(call.message.chat.id, 'Вот варианты:\n')
                for i in range(0,len(mas)):
                    if(int(mas[i].get_square())>=100):
                        count+=1
                        p = mas[i].display_place()
                        bot.send_message(call.message.chat.id, f" {p}")
                if(count==0):
                    bot.send_message(call.message.chat.id,"К сожалению вариантов не нашлось , попробуйте позже")



            elif call.data == 'bad':
                bot.send_message(call.message.chat.id, 'Можем предложить такие варианты:')
                count2=0
                for i in range(0,len(mas)):
                    if(int(mas[i].get_square())<100):
                        count2+=1
                        p = mas[i].display_place()
                        bot.send_message(call.message.chat.id, f" {p}")
                if(count2==0):
                    bot.send_message(call.message.chat.id,"К сожалению вариантов не нашлось , попробуйте позже")
 
 
            # show alert
            bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                text="ЭТО ТЕСТОВОЕ УВЕДОМЛЕНИЕ!!11")
 
    except Exception as e:
        print(repr(e))
 
# RUN
bot.polling(none_stop=True)