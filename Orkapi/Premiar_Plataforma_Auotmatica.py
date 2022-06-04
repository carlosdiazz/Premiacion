import schedule
from Funciones_Necesarias import fecha, borrarPantalla, saber_Nombre_Loteria_Sorteo, Peticion_GET
import time
from ORKAPI import ORKAPI
from Funciones_para_buscar_premios import sendNotification

class Premiar_Loterias_():

    def __init__(self, loteriaARG):
        print('Inicio el Proceso de Premiacion')
        self.Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteriaARG)
        self.intentos = 0

    def Premiar_Loterias(self):

        nombre_loteria = self.Nombre_loteria_sorteo[0]
        nombre_Sorteo = self.Nombre_loteria_sorteo[1]
        respuesta = f'PUBLICANDO EN PLATAFORMA PARA LA LOTERIA: {nombre_loteria} CON EL SORTEO {nombre_Sorteo}'
        intentos = self.intentos
        fecha_ahorAA = fecha('%d-%m-%Y')
        peticion = Peticion_GET(nombre_Sorteo,fecha_ahorAA)

        if(intentos <= 90) :
            intentos = intentos + 1

            if(type(peticion) == dict):
                numeros_a_publicar = peticion['numeros_ganadores']
                result = ORKAPI(nombre_loteria,nombre_Sorteo,numeros_a_publicar)
                if(result[0]):
                    print(f'INTENTO #{intentos}')
                    print(f'SE PUBLICO BIEN ----> {result[1]}')
                    respuesta = result[1]
                    intentos=100
                    self.Premiar_Loterias()
                else:
                    print(f'\n\nINTENTO #{intentos}\n\n')
                    print(f'\n\nSIGUE INTENTANDO NO SE PUBLICO ----> {result[1]}')
                    time.sleep(20)
                    respuesta = result[1]
                    self.Premiar_Loterias()
            else:
                print(f'\n\nINTENTO #{intentos}\n\n')
                print(f'\n\nERROR --> PREMIAR PLATAFORMA --> LOTERIA: {nombre_loteria} Sorteo: {nombre_Sorteo} ---> {peticion}\n\n')
                time.sleep(20)
                self.respuesta = peticion
                self.Premiar_Loterias()
        else:
            print(f'\n\nPREMIAR PLATAFORMA\n\n\n--> LOTERIA: {nombre_loteria}\n--> Sorteo: {nombre_Sorteo}\n\n\n--> {respuesta}\n\n' )
            sendNotification(False,f'\n\nPREMIACION PLATAFORMA\n\n\n--> LOTERIA: {nombre_loteria}\n--> Sorteo: {nombre_Sorteo}\n\n\n--> {respuesta}' )




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
schedule.every().day.at("10:05:00").do(Anguila_AM_PREMIOS)
schedule.every().day.at("12:05:00").do(PRIMERA_AM_PREMIOS)
schedule.every().day.at("12:30:00").do(LA_SUERTE_PREMIOS)
schedule.every().day.at("13:05:00").do(ANGUILA_MD_PREMIOS)
schedule.every().day.at("13:10:00").do(REAL_PREMIOS)
schedule.every().day.at("13:50:00").do(FLORIDA_AM_PREMIOS)
schedule.every().day.at("14:05:00").do(LOTEDOM_PREMIOS)
schedule.every().day.at("14:35:00").do(NEW_YORK_AM_PREMIOS)
schedule.every().day.at("14:40:00").do(Ganams_PREMIOS)
schedule.every().day.at("18:05:00").do(ANGUILA_TARDE_PREMIOS)
schedule.every().day.at("20:05:00").do(LOTEKA_PREMIOS)
schedule.every().day.at("20:05:00").do(PRIMERA_PM_PREMIOS)
schedule.every().day.at("21:10:00").do(LOTERIA_NACIONAL_PREMIOS)
schedule.every().day.at("21:11:00").do(LEIDSA_PREMIOS)
schedule.every().day.at("21:05:00").do(ANGUILA_NOCHE)
schedule.every().day.at("21:50:00").do(FLORIDA_PM_PREMIOS)
schedule.every().day.at("22:35:00").do(New_York_PM_Premios)

borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|-- PREMIOS --> {fecha_actual} <-- PREMIOS --|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(30)