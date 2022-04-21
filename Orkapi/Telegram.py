
from tokenize import Token
from turtle import update
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ORKAPI import ORKAPI
from PROCESO import PROCESO
from Funciones_Necesarias import Imprimir_Comandos
#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

#Solicitar Token
TOKEN = '5348496240:AAHvkD64i5AveuGv3v_5K1y5AyPn74MOqVg'

COMANDOS = [
    '/Start',
    "/Info",
    '/Premiar_Florida_AM',
    "/Premiar_florida_PM",
    "/Premiar_New_York_AM",
    "/Premiar_New_York_PM",
    '/Obtener_Premiar_Florida_AM',
    '/Obtener_Premiar_florida_PM',
    '/Obtener_Premiar_New_York_AM',
    '/Obtener_Premiar_New_York_PM'
]

def start(update,context):
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot, para mas informacion \n/Info")
    print(update)

def info(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado un numero random')
    message=Imprimir_Comandos(COMANDOS)
    context.bot.sendMessage(chat_id= user_id, text=message)

def echo(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id} ha enviado un mensaje')
    text = update.message.text
    context.bot.sendMessage(
        chat_id = user_id,
        text = f'Escribiste: _{text}_'
    )


def florida_AM(update, context):
    florida_am_Numeros = ORKAPI('Florida', "AM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros FLORIDA AM')
    context.bot.sendMessage(chat_id= user_id, text=florida_am_Numeros)

def florida_PM(update, context):
    florida_am_Numeros = ORKAPI('Florida', "PM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros FLORIDA PM')
    context.bot.sendMessage(chat_id= user_id, text=florida_am_Numeros)

def New_York_AM(update, context):
    New_York_numeros_am = ORKAPI('New York', "AM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros New York AM')
    context.bot.sendMessage(chat_id= user_id, text=New_York_numeros_am)

def New_York_PM(update, context):
    New_York_Numeros_PM = ORKAPI('New York', "PM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros FLORIDA PM')
    context.bot.sendMessage(chat_id= user_id, text=New_York_Numeros_PM)
#?---------------------------------------------------------------------------------------
def Obtener_florida_AM(update, context):
    florida_am_Numeros = PROCESO('Florida', "AM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros FLORIDA AM')
    context.bot.sendMessage(chat_id= user_id, text=florida_am_Numeros)

def Obtener_florida_PM(update, context):
    florida_am_Numeros = PROCESO('Florida', "PM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros FLORIDA PM')
    context.bot.sendMessage(chat_id= user_id, text=florida_am_Numeros)

def Obtener_New_York_AM(update, context):
    New_York_numeros_am = PROCESO('New York', "AM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros New York AM')
    context.bot.sendMessage(chat_id= user_id, text=New_York_numeros_am)

def Obtener_New_York_PM(update, context):
    New_York_Numeros_PM = PROCESO('New York', "PM")
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros FLORIDA PM')
    context.bot.sendMessage(chat_id= user_id, text=New_York_Numeros_PM)

if __name__ == "__main__":
    my_bot = telegram.Bot(TOKEN)
    print(my_bot)

#Enlazar nuestro upodate con nuestro bot
updater = Updater(my_bot.token, use_context=True)
#crear un despacachador
dp = updater.dispatcher

#crear los manejadores
dp.add_handler(CommandHandler('Start',start))
dp.add_handler(CommandHandler('Info',info))
#?---------------------------------------------------------------
dp.add_handler(CommandHandler('Premiar_Florida_AM',florida_AM))
dp.add_handler(CommandHandler('Premiar_florida_PM',florida_PM))
dp.add_handler(CommandHandler('Premiar_New_York_AM',New_York_AM))
dp.add_handler(CommandHandler('Premiar_New_York_PM',New_York_PM))
#?----------------------------------------------------------------
dp.add_handler(CommandHandler('Obtener_Premiar_Florida_AM',Obtener_florida_AM))
dp.add_handler(CommandHandler('Obtener_Premiar_florida_PM',Obtener_florida_PM))
dp.add_handler(CommandHandler('Obtener_Premiar_New_York_AM',Obtener_New_York_AM))
dp.add_handler(CommandHandler('Obtener_Premiar_New_York_PM',Obtener_New_York_PM))
#?----------------------------------------------------------------
dp.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
print("EL bot se Cargo Correctamente")
updater.idle()