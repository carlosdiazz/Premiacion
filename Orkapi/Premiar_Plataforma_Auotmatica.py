import schedule
from Funciones_Necesarias import fecha, borrarPantalla, saber_Nombre_Loteria_Sorteo, Peticion_GET, Obtener_User_MONGO_NOTIFICACIONES
import time
from ORKAPI import ORKAPI
import requests
from TOKEN_API_PRO_DE import TOKEN_NOTIFICACION_PLATAFORMA_DESARROLLO
import threading
def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

def sendNotification(message ):
    try:
        bot_token = TOKEN_NOTIFICACION_PLATAFORMA_DESARROLLO
        User=Obtener_User_MONGO_NOTIFICACIONES()
        for usuarios in User:
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + usuarios + '&parse_mode=Markdown&text=' + message
            requests.get(send_text)

    except:
        print('-----------------------------------------------------------------------')
        print("NO SE PUEDO ENVIAR LA NOTIFICACION DE TELEGRAM")
        print('-----------------------------------------------------------------------')
        time.sleep(10)

class Premiar_Loterias_():

    def __init__(self, loteriaARG):
        print('Inicio el Proceso de Premiacion')
        self.Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteriaARG)
        self.intentos = 0
        nombre_loteria = self.Nombre_loteria_sorteo[0]
        nombre_Sorteo = self.Nombre_loteria_sorteo[1]
        self.respuesta = f'\n\nCOMENZO EL PROCESO PARA PREMIAR EN PLATAFORMA PARA LA LOTERIA: {nombre_loteria} CON EL SORTEO {nombre_Sorteo}\n\n'

    def Premiar_Loterias(self):

        nombre_loteria = self.Nombre_loteria_sorteo[0]
        nombre_Sorteo = self.Nombre_loteria_sorteo[1]
        fecha_ahorAA = fecha('%d-%m-%Y')
        peticion = Peticion_GET(nombre_Sorteo,fecha_ahorAA)

        if(self.intentos <= 90) :
            self.intentos = self.intentos + 1

            if(type(peticion) == dict):
                numeros_a_publicar = peticion['numeros_ganadores']
                result = ORKAPI(nombre_loteria,nombre_Sorteo,numeros_a_publicar)
                if(result[0]):
                    print(f'INTENTO #{self.intentos}')
                    print(f'SE PUBLICO BIEN ----> {result[1]}')
                    self.respuesta = result[1]
                    self.intentos=100
                    self.Premiar_Loterias()

                else:
                    print(f'\n\nINTENTO #{self.intentos}\n\n')
                    print(f'\n\nSIGUE INTENTANDO NO SE PUBLICO ----> {result[1]}')
                    time.sleep(20)
                    self.respuesta = result[1]
                    self.Premiar_Loterias()
            else:
                print(f'\n\nINTENTO #{self.intentos}\n\n')
                print(f'\n\nERROR --> PREMIAR PLATAFORMA --> LOTERIA: {nombre_loteria} Sorteo: {nombre_Sorteo} ---> {peticion}\n\n')
                time.sleep(20)
                self.respuesta = peticion
                self.Premiar_Loterias()
        else:
            print(f'\n\nPREMIAR PLATAFORMA\n\n\n--> LOTERIA: {nombre_loteria}\n--> Sorteo: {nombre_Sorteo}\n\n\n--> {self.respuesta}\n\n' )
            sendNotification(f'\n\nPREMIACION PLATAFORMA\n\n\n--> LOTERIA: {nombre_loteria}\n--> Sorteo: {nombre_Sorteo}\n\n\n--> {self.respuesta}' )
            self.intentos=0



Anguila_AM_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_AM').Premiar_Loterias
PRIMERA_AM_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Primera_AM').Premiar_Loterias
LA_SUERTE_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Suerte').Premiar_Loterias
ANGUILA_MD_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_MD').Premiar_Loterias
REAL_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Real').Premiar_Loterias
FLORIDA_AM_PREMIOS = Premiar_Loterias_('/Premiar_Florida_AM').Premiar_Loterias
LOTEDOM_PREMIOS = Premiar_Loterias_('/Premiar_Lotedom').Premiar_Loterias
NEW_YORK_AM_PREMIOS = Premiar_Loterias_('/Premiar_New_York_AM').Premiar_Loterias
Ganams_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Ganamas').Premiar_Loterias
ANGUILA_TARDE_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_TARDE').Premiar_Loterias
LOTEKA_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Loteka').Premiar_Loterias
PRIMERA_PM_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Primera_PM').Premiar_Loterias
LOTERIA_NACIONAL_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Nacional').Premiar_Loterias
LEIDSA_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Leidsa').Premiar_Loterias
ANGUILA_NOCHE = Premiar_Loterias_('/Premiar_Anguila_NOCHE').Premiar_Loterias
FLORIDA_PM_PREMIOS = Premiar_Loterias_('/Premiar_Florida_PM').Premiar_Loterias
New_York_PM_Premios = Premiar_Loterias_('/Premiar_New_York_PM').Premiar_Loterias


#! ---------------------------------------------------------
schedule.every().day.at("10:05:00").do(run_threaded, Anguila_AM_PREMIOS)
schedule.every().day.at("12:05:00").do(run_threaded, PRIMERA_AM_PREMIOS)
schedule.every().day.at("12:35:00").do(run_threaded, LA_SUERTE_PREMIOS)
schedule.every().day.at("13:05:00").do(run_threaded, ANGUILA_MD_PREMIOS)
schedule.every().day.at("13:05:00").do(run_threaded, REAL_PREMIOS)
schedule.every().day.at("13:50:00").do(run_threaded, FLORIDA_AM_PREMIOS)
schedule.every().day.at("14:05:00").do(run_threaded, LOTEDOM_PREMIOS)
schedule.every().day.at("14:35:00").do(run_threaded, NEW_YORK_AM_PREMIOS)
schedule.every().day.at("14:40:00").do(run_threaded, Ganams_PREMIOS)
schedule.every().day.at("18:05:00").do(run_threaded, ANGUILA_TARDE_PREMIOS)
schedule.every().day.at("20:05:00").do(run_threaded, LOTEKA_PREMIOS)
schedule.every().day.at("20:05:00").do(run_threaded, PRIMERA_PM_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, LOTERIA_NACIONAL_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, LEIDSA_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, ANGUILA_NOCHE)
schedule.every().day.at("21:50:00").do(run_threaded, FLORIDA_PM_PREMIOS)
schedule.every().day.at("22:35:00").do(run_threaded, New_York_PM_Premios)
#!--------------------------------DOMINGO-------------------------------
schedule.every().sunday.at("15:55:00").do(run_threaded, LEIDSA_PREMIOS)
schedule.every().sunday.at("18:05:00").do(run_threaded, LOTERIA_NACIONAL_PREMIOS)


borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|-- PREMIOS --> {fecha_actual} <-- PREMIOS --|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(60)