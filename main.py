import telebot
#import requestes
import mysql.connector
import itertools


# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="turk",
#     database="telebot"
# )

# mycursor = mydb.cursor()

# cod=("select aval from chat")


# mycursor.execute(cod)

# mydb.commit()

# a = mycursor.fetchall()
# n=list(itertools.chain(*a))
# for i in n:
#     print(i)


bot=telebot.TeleBot("6475579094:AAHBPrfikf1LT51Kfvn4ZMGLlHlhJCHKx1k") #@testpythonpouyabot

@bot.message_handler(commands=['start', 'help'])
def start_message(mesage):
    bot.reply_to(mesage,"سلام چه کمکی میتونم کنم")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    if message.text=="سلام":
        bot.reply_to(message,"خوبی")
    elif  message.text=="خوبم تو خوبی":
        bot.reply_to(message,"منم خوبم")
    elif message.text=="پویا کیه؟":
        bot.reply_to(message,"سازندمه")
    else:
        bot.reply_to(message, message.text)

@bot.message_handler(content_type=['document', 'audio',])
def coment_type(mesage):
    bot.reply_to(mesage,"چی فرستادی داوشم")

@bot.message_handler(regexp="SOME_REGEXP")
def handle_message(mesage):
    bot.reply_to(mesage, "تست")

# @bot.message_handler(func=lambda message: True)
# def price(mesage):
#     a=mesage.text.upper()
#     b=requestes.get()
#     if b.re

bot.infinity_polling()
