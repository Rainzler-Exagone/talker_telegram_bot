import os
import telebot
from dotenv import load_dotenv

load_dotenv()
 
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)

@bot.message_handler(commands=['start'])

def greet(message):
    bot.reply_to(message,"Hi! how is it going ?")

@bot.message_handler(commands=['Greet'])

def greet(message):
    bot.reply_to(message,"Hi! how is it going ?")

bot.polling()



