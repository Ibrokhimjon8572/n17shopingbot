import telegram
import telebot
from telebot.types import Message

BOT_TOKEN='6518843395:AAE8hvmphw_cw25k9Mq2VEilaBXGtj1bnZY'

bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_handler(msg:Message):
    bot.send_message(msg.chat.id, "Shopping bot ga hush kelibsiz!!")

