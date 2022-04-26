import telegram
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from ORKAPI import ORKAPI
from Funciones_Necesarias import Imprimir_Comandos, Saber_loteria_Plataforma
from Doble_Check import Doble_Check
from NOMBRES_VARIABLES import COMANDOS, Comandos_Premios, Comandos_Resultados
from Funciones_Necesarias import borrarPantalla
#Configurar Logging
logging.basicConfig(
    level = logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger()

from Funciones_Necesarias import fecha, saberLoteria, saberNombreLoteria, saber_si_loteria_es_anguila
#Solicitar Token
from TOKEN_API_PRO_DE import TOKEN

Premios_HOY = {

}

def obtener_Premio(loteria):
    fechaHOY = fecha('%d-%m-%Y')
    if fechaHOY in Premios_HOY.keys():
        if loteria in Premios_HOY[fechaHOY]:
            #SI la loteria exsite y es la fecha de hoy devuelve los numeros
                return Premios_HOY[fechaHOY][loteria]
        else:
            return False
    else:
        return False

def obtener_Numero(loteria):
    fechaHOY = fecha('%d-%m-%Y')
    #?AQUI ENTRA SI LA FECHA YA ESTA PUBLICADA
    if fechaHOY in Premios_HOY.keys():
        if loteria in Premios_HOY[fechaHOY]:
            #SI la loteria exsite y es la fecha de hoy devuelve los numeros
                return Premios_HOY[fechaHOY][loteria]
        else:
            loteriaARREGLO = saberLoteria(loteria)
            numeros = Doble_Check(loteriaARREGLO)

            if(numeros):
                Premios_HOY[fechaHOY][loteria]=numeros
                return numeros
            else:
                return 'LOS NUMEROS AUN NO HAN SIDOS PUBLICADOS EN LA PAGINA OFICIAL'

    else:
        #? TEngo aqui que agregar la nueva fecha para seguir el proceso
        loteriaARREGLO = saberLoteria(loteria)
        numeros = Doble_Check(loteriaARREGLO )
        if(numeros):
            Premios_HOY[fechaHOY]={loteria:numeros}
            return numeros
        return 'LOS NUMEROS AUN NO HAN SIDOS PUBLICADOS EN LA PAGINA OFICIAL'

def start(update,context):
    borrarPantalla()
    logger.info(f"El usuario {update.effective_user['username']}, ha iniciado una conversacion")
    name = update.effective_user['first_name']
    update.message.reply_text(f"Hola {name} soy tu Bot, para mas informacion \n/Info")
    print(update)

def info(update, context):
    borrarPantalla()
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Imprimir_Comandos(COMANDOS)
    context.bot.sendMessage(chat_id= user_id, text=message)

def VERTODO(update, context):
    borrarPantalla()
    user_id = update.effective_user['id']
    logger.info(f'El usuario {user_id}, ha solicitado ver informacion')
    message=Premios_HOY
    context.bot.sendMessage(chat_id= user_id, text=message)

def Comandos_Resul(update, context):
    borrarPantalla()
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
    borrarPantalla()
    logger.info('Inicio el proceso de Premiacion')
    user_id = update.effective_user['id']
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Premiacion')
    loteria_selecionada = update.message.text
    nombre_loteria = saberNombreLoteria(loteria_selecionada)
    loterias = Saber_loteria_Plataforma(nombre_loteria)
    print(loterias)
    loteria = loterias[0]
    horario = loterias[1]
    premios = obtener_Premio(nombre_loteria)
    if(premios):
        Numeros = ORKAPI(loteria, horario, premios)
        logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros')
        context.bot.sendMessage(chat_id= user_id, text=Numeros)
    else:
        logger.info(f'El usuario {user_id}, ha mandado a publicar los numeros')
        logger.info(f'NO SE PREMIO PORQUE LOS RESULTADOS NO ESTAN')
        context.bot.sendMessage(chat_id= user_id, text='NO SE PREMIO PORQUE LOS RESULTADOS NO ESTAN')

def Obtener_numeros_loteria(update, context):
    borrarPantalla()
    logger.info('Inicio el proceso de Buscar Numeros')
    user_id = update.effective_user['id']
    context.bot.sendMessage(chat_id= user_id, text='Inicio el Proceso de Buscar el Resultado')
    loteria_selecionada = update.message.text
    saber_loteria = saberNombreLoteria(loteria_selecionada)
    NUMEROS_CORRECTOS = obtener_Numero(saber_loteria)
    logger.info(f'El usuario {user_id}, ha mandado a ver los numeros ')
    context.bot.sendMessage(chat_id= user_id, text=NUMEROS_CORRECTOS)
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