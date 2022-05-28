
import telebot
from telebot import types
bot = telebot.TeleBot("5320653955:AAFLZ9_nwCyR6IFQ6ZPsiNQQ45z4R6-LULI")
@bot.message_handler(commands=['start', 'домики'])
def start(message):
    global user_data
    user_data = []
    mess = f'Здравствуйте! Хотите узнать подробнее о курсе "Домики" 🏘️?Кликните на кнопку ниже, уважаемый {message.from_user.last_name }'
    bot.send_message(message.chat.id,mess,parse_mode='html')
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    itembtn1 = types.KeyboardButton('Узнать о курсе')
    markup.add(itembtn1)
    bot.send_message(message.chat.id, "Кликните на кнопку ниже", reply_markup=markup)
@bot.message_handler()    
def sent_to_sales(message):
    lid_message = f'С вами свяжется мой помощник и расскажет все о курсе. Напишите ваш номер телефона'
    sent_get_message = bot.send_message(message.chat.id,lid_message,parse_mode='html')
    bot.register_next_step_handler(sent_get_message , get_user_phone)
def get_user_phone(message):
    sent_get_user_name = bot.send_message(message.chat.id,'А теперь напишите ваше имя',parse_mode='html')
    bot.register_next_step_handler(sent_get_user_name , get_user_name)
    user_phone = message.text
    user_data.append(user_phone)
def get_user_name(message):
    bot.send_message(message.chat.id,'До свидания, с вами свяжется специалист',parse_mode='html')
    user_name = message.text
    user_data.append(user_name)
    print(user_data)









bot.polling(none_stop=True)