
1- Lo primero es crear un archivo de python que se llame TOKEN_API_PRO_DE.py, donde incluira todos los tokens

Las estrutuctura es de la siguiente forma
#---------------------------------------------------------------------------------------------------
#!AQUI ESTAN TODAS LAS API IMPORTANTES DE MI APLICACION Y TODA LA ESTRCUTURA

#? Configuracion Correo del que salen los emails
CORREO = 'correo@hotmail.com'
PASS_CORREO = '000'

#?Configuracion MONGO DB
API_KEY_MONGO_DB = 'API DE MONGO'

#? TOKEN PARA NOTIFICACIONES DE NUMEROS PUBLICADOS
TOKEN_NOTIFICACION = 'TOKEN_TELEGRAM'

#? TOKEN PRODUCION BOT PADRE
TOKEN = 'TOKEN_TELEGRAM'

#? TOKEN TEST BOT PADRE
#TOKEN ='TOKEN_TELEGRAM'


plataforma_Desarrollo = {
    'token'         :   'TOKEN_TELEGRAM',
    'url'           :   'URL_PLATAFORMA',
    'username'      :   'USER',
    'password'      :   'PASS',
    'plataforma'    :   'Desarrollo'
}

plataforma_Mega_Lottery = {
    'token'         :   'TOKEN_TELEGRAM',
    'url'           :   'URL_PLATAFORMA',
    'username'      :   'USER',
    'password'      :   'PASS',
    'plataforma'    :   'MegaLottery'
}

plataforma_Rapidita = {
    'token'         :   'TOKEN_TELEGRAM',
    'url'           :   'URL_PLATAFORMA',
    'username'      :   'USER',
    'password'      :   'PASS',
    'plataforma'    :   'Rapidita'
}
#---------------------------------------------------------------------------------------------------

2- Debemois tambien de correr el servidor de Expres, para correrlos lo ejecuto con npm run start


3- Para ejecutar el programa, necesitamos abrir 3 archivos de pyhton indepedientes...

- python3 Telegram.py = Funciona para activar el bot padre el cual nos suscribe a la base de datos, y nos manda los link de los demas boot

- pyhton3 Premiar_Plataformas_Automaticas.py = Es el script que se encargar de premiar todas las plataforma dependiendo su configuracion

- pyhton3 Publicar_Numeros_diario.py = Es el script que se encarga de obtener los diferentes numeros de forma automaticas

4- Si todo sale bien, este programa se conecta a la diferentes fuentes de la loterias, coge la data y la publica en nuestra base de datos en Mongo DB, para luego el script se encargar de publicar los numeros en las diferentes plataformas