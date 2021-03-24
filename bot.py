import time
import schedule
import telebot
from datetime import datetime

bot = telebot.TeleBot('1758490944:AAEzDcrkuilDBulhlNOzwb3UboeveZ9qw-0')
now = datetime.now()
current_time = now.strftime("%H:%M")
print("Current Time =", current_time)
if current_time=='18:34':
    test_send_message()
time.sleep(1)

users = []
uclass = []

def send_message():
        text = 'У тебя урок через минуту!'
        for user in users:
            ret_msg = bot.send_message(user, text)
            assert ret_msg.message_id 
        
@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    if message.from_user.id not in users:
        users.append(message.from_user.id)
        uclass.append(0)
    print(users, uclass)
    bot.reply_to(message, f'Я бот расписания Школы №1561. Приятно познакомиться, {message.from_user.first_name}\nЧтобы узнавать расписание звонков напиши номер своего класса (7 - 11).\nПосмотреть все мои возможности - /commands')
    send_message()
     
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text.lower() == 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    elif message.text.lower() == '7':
        bot.send_message(message.from_user.id, 'Хорошо, ученик 7 класса! Скоро я пришлю тебе сообщение о начале урока.')
        #for user in users:
        #    if user 
    elif message.text.lower() == '8':
        bot.send_message(message.from_user.id, 'Хорошо, ученик 8 класса! Скоро я пришлю тебе сообщение о начале урока.')
    elif message.text.lower() == '9':
        bot.send_message(message.from_user.id, 'Хорошо, ученик 9 класса! Скоро я пришлю тебе сообщение о начале урока.')
    elif message.text.lower() == '10':
        bot.send_message(message.from_user.id, 'Хорошо, ученик 10 класса! Скоро я пришлю тебе сообщение о начале урока.')
    elif message.text.lower() == '11':
        bot.send_message(message.from_user.id, 'Хорошо, ученик 11 класса! Скоро я пришлю тебе сообщение о начале урока.')
    else:
        bot.send_message(message.from_user.id, 'Не понимаю, что это значит.')
 
bot.polling(none_stop=True)
