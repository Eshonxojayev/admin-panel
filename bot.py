import os
import telebot
import psycopg2 as db
import time
from dotenv import load_dotenv
data = load_dotenv()
# Bot tokenini kiritib olamiz
BOT_TOKEN = os.getenv('6706829652:AAEBagqfDRh-zYetZ1bU8PV0xptVIImurAY')
bot = telebot.TeleBot('6706829652:AAEBagqfDRh-zYetZ1bU8PV0xptVIImurAY')

# @bot.message_handler(func=lambda msg: True)
# def echo_all(message):
#     bot.reply_to(message, "Hi Ruslan, what's up")

class Database:
    @staticmethod
    def connect(query, query_type):
        database = db.connect(
            database="lesson_5_6oy",
            user="postgres",
            host="localhost",
            password="2160607",
            port="5432"
        )
        cursor = database.cursor()
        cursor.execute(query)
        data = ['insert', 'create', 'delete', 'update']
        if query_type in data:
            database.commit()
            return "Success"

        else:
            return cursor.fetchall()

@bot.message_handler(commands=['data'])
def data(message):
    query = 'SELECT * FROM auth_user'
    data = Database.connect(query, "select")
    bot.reply_to(message, f"{data}")

@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    print(f"{message.from_user.username}")
    bot.reply_to(message, f"{message.from_user} ")

if __name__ == "__main__":
    bot.infinity_polling()