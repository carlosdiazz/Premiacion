
from tokenize import Token
from turtle import update
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import random
from ORKAPI import main

#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

#Solicitar Token
TOKEN = '5348496240:AAHvkD64i5AveuGv3v_5K1y5AyPn74MOqVg'

def start(update,context):
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado hablar")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot")
    print(update)

def Ale(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado un numero random')
    number = random.randint(0,10)
    context.bot.sendMessage(chat_id= user_id, text=f'El numero aleatorio es: {number}')

def info(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado un numero random')
    context.bot.sendMessage(chat_id= user_id, text=f'/start \n /random \n /Florida_AM \n /NewYork_AM')

def florida(update, context):
    ok=main(True, 'Florida', 'AM').prueeee
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado un numero random')
    context.bot.sendMessage(chat_id= user_id, text=ok)

def newYork(update, context):
    ok2=main(True, 'New York', 'AM').prueeee
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado un numero random')
    context.bot.sendMessage(chat_id= user_id, text=ok2)


def echo(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id} ha enviado un mensaje')
    text = update.message.text
    context.bot.sendMessage(
        chat_id = user_id,
        text = f'Escribiste: _{text}_'
    )


if __name__ == "__main__":
    my_bot = telegram.Bot(TOKEN)
    print(my_bot)

#Enlazar nuestro upodate con nuestro bot
updater = Updater(my_bot.token, use_context=True)

#crear un despacachador
dp = updater.dispatcher

#crear los manejadores
dp.add_handler(CommandHandler('start',start))
dp.add_handler(CommandHandler('random',Ale))
dp.add_handler(CommandHandler('Florida_AM',florida))
dp.add_handler(CommandHandler('NewYork_AM',newYork))
dp.add_handler(CommandHandler('info',info))
dp.add_handler(MessageHandler(Filters.text,echo))


updater.start_polling()
print("EL bot se Cargo")
updater.idle()