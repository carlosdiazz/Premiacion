from tkinter import PhotoImage
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ORKAPI import ORKAPI
from Funciones_Necesarias import Imprimir_Comandos, Peticion_GET, fecha, imprimir_resultados
from NOMBRES_VARIABLES import COMANDOS, Comandos_Premios, Comandos_Resultados
from os import remove
#from borrar import mandar
#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

from Funciones_Necesarias import fecha,  saber_Nombre_Loteria_Sorteo
#Solicitar Token
from TOKEN_API_PRO_DE import TOKEN

def start(update,context):
    #borrarPantalla()
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot, para mas informacion \n/Info")
    print(update)

def info(update, context):
    #borrarPantalla()
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Imprimir_Comandos(COMANDOS)
    context.bot.sendMessage(chat_id= user_id, text=message)

def VERTODO(update, context):
    #borrarPantalla()
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Premios_HOY
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
    user_id = update.effective_user['id']
    logger.info('Inicio el proceso de Premiacion')
    logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros')
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Premiacion')
    loteria_selecionada = update.message.text
    Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteria_selecionada)
    loteria = Nombre_loteria_sorteo[0]
    sorteo = Nombre_loteria_sorteo[1]
    fecha_AHORA = fecha('%d-%m-%Y')
    peticion_GET = Peticion_GET(sorteo,'28-04-2022')

    if(type(peticion_GET)==dict):

        numeros_a_publicar = peticion_GET['numeros_ganadores']
        result = ORKAPI(loteria,sorteo,numeros_a_publicar)
        if(result[0]):
            context.bot.sendMessage(chat_id= user_id, text=result[1])
            context.bot.sendPhoto(chat_id= user_id, photo=open('./premiada.png','rb'))
            remove('./premiada.png')
        else:
            context.bot.sendMessage(chat_id= user_id, text=result[1])
    else:
        print(peticion_GET)
        logger.info(peticion_GET)
        context.bot.sendMessage(chat_id= user_id, text=peticion_GET)

def Obtener_numeros_loteria(update, context):
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros ')
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Buscar el Resultado')
    loteria_selecionada = update.message.text
    Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteria_selecionada)
    sorteo = Nombre_loteria_sorteo[1]
    fecha_AHORA = fecha('%d-%m-%Y')
    peticion_GET = Peticion_GET(sorteo,fecha_AHORA)
    resultado = imprimir_resultados(peticion_GET)
    context.bot.sendMessage(chat_id= user_id, text=resultado)
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
dp.add_handler(CommandHandler('TODO',VERTODO))
dp.add_handler(CommandHandler('Premiar',Comandos_Premiar))
dp.add_handler(CommandHandler('Ver_Resultados',Comandos_Resul))
#?---------------------------------------------------------------
dp.add_handler(CommandHandler('Premiar_Florida_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Florida_PM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_New_York_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_New_York_PM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Real',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Suerte',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Leidsa',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Nacional',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Ganamas',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Loteka',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Primera_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Primera_PM',Premiar_Loterias))
#?----------------------------------------------------------------
dp.add_handler(CommandHandler('Obtener_Florida_AM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Florida_PM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_New_York_AM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_New_York_PM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_Real',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_Ganamas',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_Nacional',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_Loteka',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_Leidsa',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_La_Suerte',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_La_Primera_AM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Loteria_La_Primera_PM',Obtener_numeros_loteria))
#! ------------------------------------------------------------------------------
# dp.add_handler(CommandHandler('Obtener_Anguila_AM',Obtener_numeros_loteria))
# dp.add_handler(CommandHandler('Obtener_Anguila_MD',Obtener_numeros_loteria))
# dp.add_handler(CommandHandler('Obtener_Anguila_Tarde',Obtener_numeros_loteria))
# dp.add_handler(CommandHandler('Obtener_Anguila_PM',Obtener_numeros_loteria))
#?----------------------------------------------------------------
dp.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
print("EL bot se Cargo Correctamente")
updater.idle()