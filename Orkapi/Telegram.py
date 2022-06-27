from tkinter import PhotoImage
import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ORKAPI import ORKAPI
from Funciones_Necesarias import Imprimir_Comandos, Peticion_GET, fecha, imprimir_resultados, Verificar_si_un_usuario_existe, Agregar_Nuevo_Usuario_MONGODB, borrarPantalla
from NOMBRES_VARIABLES import COMANDOS, Comandos_Premios, Comandos_Resultados, Comandos_Forzarr_Premios
from FUncion_Necesaria_FOrzar_Premio import Saber_Loteria_Forzada_Premio

url = 'https://dev_admin.orkapi.net/'
username = 'carlos@premio'
password = 1234

#! Este es el bot Padre donde podre suscibirme a lso diferentes canales para recibir notificaciones

#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

from Funciones_Necesarias import fecha,  saber_Nombre_Loteria_Sorteo
#Solicitar Token
from TOKEN_API_PRO_DE import TOKEN

def start(update,context):
    logger.info(f"\nEl usuario {update.effective_user['username']}, ha iniciado una conversacion\n")
    user_id = update.effective_user['id']
    Validar=Verificar_si_un_usuario_existe(str(user_id))
    if(Validar == True):
        Agregar_Nuevo_Usuario_MONGODB(str(user_id))
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot para premiar, para mas informacion \n/Info \n\n\nBot de NOTIFICACIONES:\n\nhttp://t.me/Notificacion_premio_bot \n\n\nBot de NOTIFICACIONES MEGA LOTTERY:\n\nhttp://t.me/PremiosMegaLotery_bot\n\n\nBot de NOTIFICACIONES DESARROLLO:\n\nhttp://t.me/PremiosDesarrollo_bot\n\n\nBot de NOTIFICACIONES RAPIDITA:\n\nhttp://t.me/PremiacionRapidita_bot")
    print(update)

def info(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha solicitado ver informacion\n')
    message=Imprimir_Comandos(COMANDOS)
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Resul(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha solicitado ver informacion\n')
    message=Imprimir_Comandos(Comandos_Resultados)
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Forzar_Premios(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha solicitado ver informacion\n')
    message=Imprimir_Comandos(Comandos_Forzarr_Premios)
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Premiar(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha solicitado ver informacion\n')
    message=Imprimir_Comandos(Comandos_Premios)
    context.bot.sendMessage(chat_id= user_id, text=message)

def echo(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id} ha enviado un mensaje\n')
    text = update.message.text
    context.bot.sendMessage(
        chat_id = user_id,
        text = f'Escribiste: _{text}_'
    )

def Premiar_Loterias(update, context):
    user_id = update.effective_user['id']
    logger.info('\nInicio el proceso de Premiacion\n')
    logger.info(f'\nEl usuario {user_id}, ha mandado a publicar los numeros\n')
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Premiacion')
    loteria_selecionada = update.message.text
    Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteria_selecionada)
    loteria = Nombre_loteria_sorteo[0]
    sorteo = Nombre_loteria_sorteo[1]
    fecha_AHORA = fecha('%d-%m-%Y')
    #! --------
    peticion_GET = Peticion_GET(sorteo,fecha_AHORA)

    if(type(peticion_GET)==dict):

        numeros_a_publicar = peticion_GET['numeros_ganadores']
        result = ORKAPI(loteria,sorteo,numeros_a_publicar,url,username,password)
        if(result[0]):
            context.bot.sendMessage(chat_id= user_id, text=result[1])
            context.bot.sendPhoto(chat_id= user_id, photo=open('./premiada.png','rb'))
            #remove('./premiada.png')
        else:
            context.bot.sendMessage(chat_id= user_id, text=result[1])
    else:
        print(peticion_GET)
        logger.info(peticion_GET)
        context.bot.sendMessage(chat_id= user_id, text=peticion_GET)

def Obtener_numeros_loteria(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha mandado a ver los numeros \n')
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Buscar el Resultado')
    loteria_selecionada = update.message.text
    Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteria_selecionada)
    sorteo = Nombre_loteria_sorteo[1]
    fecha_AHORA = fecha('%d-%m-%Y')
    #! -----
    peticion_GET = Peticion_GET(sorteo,fecha_AHORA)
    print(peticion_GET)
    resultado = imprimir_resultados(peticion_GET)
    context.bot.sendMessage(chat_id= user_id, text=resultado)

def Forzar_Premios(update, context):
    user_id = update.effective_user['id']
    logger.info(f'\nEl usuario {user_id}, ha mandado A forzar la premiacion  \n')
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso Forzado de Premiacion')
    Saber_Loteria_Forzada_Premio(update.message.text)

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
dp.add_handler(CommandHandler('Premiar_Loteria_Real',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Suerte',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Leidsa',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Nacional',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Ganamas',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_Loteka',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Primera_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Loteria_La_Primera_PM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Lotedom',Premiar_Loterias))
#!----------------------------------------------------------------
dp.add_handler(CommandHandler('Premiar_Anguila_AM',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Anguila_MD',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Anguila_TARDE',Premiar_Loterias))
dp.add_handler(CommandHandler('Premiar_Anguila_NOCHE',Premiar_Loterias))
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
dp.add_handler(CommandHandler('Obtener_Lotedom',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_King_Lottery_AM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_King_Lottery_PM',Obtener_numeros_loteria))
#! ------------------------------------------------------------------------------
dp.add_handler(CommandHandler('Obtener_Anguila_AM',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Anguila_MD',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Anguila_Tarde',Obtener_numeros_loteria))
dp.add_handler(CommandHandler('Obtener_Anguila_PM',Obtener_numeros_loteria))
#?----------------------------------------------------------------
dp.add_handler(CommandHandler('FORZAR',Comandos_Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Anguila_AM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_La_Primera_AM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Loteria_La_Suerte', Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_King_LT_MD', Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Loteria_Real',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Anguila_MD',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Florida_AM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Lotedom',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_New_York_AM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Anguila_TARDE',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_King_LT_PM', Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Loteria_Loteka',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_La_Primera_PM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Loteria_Nacional',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Loteria_Leidsa',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Anguila_NOCHE',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_Florida_PM',Forzar_Premios))
dp.add_handler(CommandHandler('Forzar_Premiar_New_York_PM',Forzar_Premios))

dp.add_handler(MessageHandler(Filters.text,echo))

updater.start_polling()
borrarPantalla()
print("EL bot se Cargo Correctamente")
updater.idle()