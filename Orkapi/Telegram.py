import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ORKAPI import ORKAPI
from PROCESO import PROCESO
from Funciones_Necesarias import Imprimir_Comandos
from saber_loteria import saberloteriaBOT
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
    "/Premiar",
    "/Ver_Resultados"
]

Comandos_Premios =[
    '/Premiar_Florida_AM',
    "/Premiar_Florida_PM",
    "/Premiar_New_York_AM",
    "/Premiar_New_York_PM",
    "/Premiar_Real"
]

Comandos_Resultados = [
    '/Obtener_Florida_AM',
    '/Obtener_Florida_PM',
    '/Obtener_New_York_AM',
    '/Obtener_New_York_PM'
]

def start(update,context):
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot, para mas informacion \n/Info")
    print(update)

def info(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Imprimir_Comandos(COMANDOS)
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Resul(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Imprimir_Comandos(Comandos_Resultados)
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Premiar(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Imprimir_Comandos(Comandos_Premios)
    context.bot.sendMessage(chat_id= user_id, text=message)

def echo(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id} ha enviado un mensaje')
    text = update.message.text
    context.bot.sendMessage(
        chat_id = user_id,
        text = f'Escribiste: _{text}_'
    )


def Premiar_Loterias(update, context):
    loteria_selecionada = update.message.text
    loterias = saberloteriaBOT(loteria_selecionada)
    loteria=loterias[0]
    horario=loterias[1]
    user_id = update.effective_user['id']
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Premiacion')
    Numeros = ORKAPI(loteria, horario)
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros')
    context.bot.sendMessage(chat_id= user_id, text=Numeros)

def Obtener_numeros(update, context):
    loteria_selecionada = update.message.text
    loterias = saberloteriaBOT(loteria_selecionada)
    loteria=loterias[0]
    horario=loterias[1]
    user_id = update.effective_user['id']
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Buscar el Resultado')
    numeros = PROCESO(loteria,horario)
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros ')
    context.bot.sendMessage(chat_id= user_id, text=numeros)

#?---------------------------------------------------------------------------------------


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
dp.add_handler(CommandHandler('Premiar',Comandos_Premiar))
dp.add_handler(CommandHandler('Ver_Resultados',Comandos_Resul))
#?---------------------------------------------------------------
dp.add_handler(CommandHandler('Premiar_Florida_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Florida_PM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_New_York_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_New_York_PM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Real',Premiar_Loterias))
#?----------------------------------------------------------------
dp.add_handler(CommandHandler('Obtener_Florida_AM',Obtener_numeros))
dp.add_handler(CommandHandler('Obtener_Florida_PM',Obtener_numeros))
dp.add_handler(CommandHandler('Obtener_New_York_AM',Obtener_numeros))
dp.add_handler(CommandHandler('Obtener_New_York_PM',Obtener_numeros))
#?----------------------------------------------------------------
dp.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
print("EL bot se Cargo Correctamente")
updater.idle()