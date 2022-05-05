import telegram
import logging
from telegram.ext import Updater, CommandHandler
from TOKEN_API_PRO_DE import TOKEN
from borrar import AUTOMATICO
#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()
from time import sleep
usuarios = []

def start(update):
    #borrarPantalla()
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot, para mas informacion \n/Info")
    print(update)

def info(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message="/Info"
    context.bot.sendMessage(chat_id= user_id, text=message)

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


#?----------------------------------------------------------------
while True:

    updater.start_polling()
    print("EL bot se Cargo Correctamente")
    print(AUTOMATICO())
    sleep(5)