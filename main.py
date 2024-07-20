# import os
# import telebot
# from dotenv import load_dotenv

# load_dotenv()
 
# API_KEY = os.getenv('API_KEY')
# bot = telebot.TeleBot(API_KEY)

# @bot.message_handler(commands=['start'])

# def greet(message):
#     bot.reply_to(message,"Hi! how is it going ?")

# @bot.message_handler(commands=['Greet'])

# def greet(message):
#     bot.reply_to(message,"Hi! how is it going ?")

# @bot.message_handler(commands=['work'])

# def greet(message):
#     bot.send_message(message.chat.id," hello I'm a telegram bot created to be your companion , well you wouldn't looking for bots if you are not lonly , feel sorry for you  , nah I'm joking I don't feel anything 😂 , feel free to talk whenever you want !")



# @bot.message_handler(commands=['photo'])
# def photo(message):
#  print('message.photo =', message.photo)
#  fileID = message.photo[-1].file_id
#  print('fileID =', fileID)
#  file_info = bot.get_file(fileID)
#  print('file.file_path =', file_info.file_path)
#  downloaded_file = bot.download_file(file_info.file_path)
#  with open("image.jpg", 'wb') as new_file:
#         new_file.write(downloaded_file)
# bot.polling()


import os
import telebot
from dotenv import load_dotenv
from PIL import Image
from rembg import remove
from telebot import types
import io



load_dotenv()
API_KEY = os.getenv('API_KEY')
bot = telebot.TeleBot(API_KEY)
IMAGES_DIR = 'images'


@bot.message_handler(commands=['Greet'])
def greet(message):
    bot.reply_to(message, "Hi! how is it going ?")
    

@bot.message_handler(commands=['start'])

def start(message):
    bot.send_message(message.chat.id, "Hello there it's me the talker bot let's roll")


@bot.message_handler(content_types=['photo'])
def photo(message):
 
 print('message.photo =', message.photo)
 fileID = message.photo[-1].file_id
 print('fileID =', fileID)
 file_info = bot.get_file(fileID)
 print('file.file_path =', file_info.file_path)
 downloaded_file = bot.download_file(file_info.file_path)
 if not os.path.exists(IMAGES_DIR):
         os.makedirs(IMAGES_DIR)
 file_name =  f'{IMAGES_DIR}/{fileID}.png'

 with open(file_name,'wb') as new_file:
    new_file.write(downloaded_file)

 #Removing BG and sending image
 inputPath = file_name
 outputPath = f'images/removed/{fileID}.png'


 input_image = Image.open(inputPath)
 output_image = remove(inputPath)
 output_image.save(outputPath)

 #sending processed image
 with open(outputPath,'rb') as img:
    bot.send_photo(message.chat.id,img)

 import time

 time.sleep(1)

 #removing images after sending them
#  os.remove(outputPath)
#  os.remove(inputPath)

@bot.message_handler(func = lambda message: True)
def handle_other(message):
    if message.content_type != message.text != '/start' or message.text != '/Greet':
        bot.send_message(message.chat.id, 'Send the image only! Supported formats: PNG.')

bot.polling(non_stop = True)

