import schedule
from Funciones_Necesarias import fecha, borrarPantalla, saber_Nombre_Loteria_Sorteo, Peticion_GET
import time
from ORKAPI import ORKAPI
from Funciones_para_buscar_premios import sendNotification

class Premiar_Loterias_():

    def __init__(self, loteriaARG):
        print('Inicio el Proceso de Premiacion')
        self.intentos = 0
        self.Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteriaARG)
        self.nombre_loteria = self.Nombre_loteria_sorteo[0]
        self.nombre_sorteo = self.Nombre_loteria_sorteo[1]
        self.fecha_AHORA = fecha('%d-%m-%Y')
        self.respuesta = f'PUBLICANDO EN PLATAFORMA PARA LA LOTERIA: {self.nombre_loteria} CON EL SORTEO {self.nombre_sorteo}'

    def Premiar_Loterias(self):

        peticion_GET = Peticion_GET(self.nombre_sorteo,self.fecha_AHORA)

        if(self.intentos <= 4) :
            self.intentos = self.intentos + 1

            if(type(peticion_GET) == dict):
                numeros_a_publicar = peticion_GET['numeros_ganadores']
                result = ORKAPI(self.nombre_loteria,self.nombre_sorteo,numeros_a_publicar)
                if(result[0]):
                    print(f'SE PUBLICO BIEN ----> {result[1]}')
                    self.respuesta = result[1]
                    self.intentos=100
                    self.Premiar_Loterias()
                else:
                    print(f'SIGUE INTENTANDO NO SE PUBLICO ----> {result[1]}')
                    time.sleep(1)
                    self.respuesta = result[1]
                    self.Premiar_Loterias()
            else:
                print(f'ERROR --> PREMIAR PLATAFORMA --> LOTERIA: {self.nombre_loteria} Sorteo: {self.nombre_sorteo} ---> {peticion_GET}')
                time.sleep(1)
                self.respuesta = peticion_GET
                self.Premiar_Loterias()
        else:
            print(f'\nPREMIAR PLATAFORMA\n\n\n--> LOTERIA: {self.nombre_loteria}\n--> Sorteo: {self.nombre_sorteo}\n\n\n--> {self.respuesta}' )
            sendNotification(False,f'\nPREMIAR PLATAFORMA\n\n\n--> LOTERIA: {self.nombre_loteria}\n--> Sorteo: {self.nombre_sorteo}\n\n\n--> {self.respuesta}' )




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
schedule.every().day.at("10:15:00").do(Anguila_AM_PREMIOS)
schedule.every().day.at("12:20:00").do(PRIMERA_AM_PREMIOS)
schedule.every().day.at("12:40:00").do(LA_SUERTE_PREMIOS)
schedule.every().day.at("13:10:00").do(ANGUILA_MD_PREMIOS)
schedule.every().day.at("13:15:00").do(REAL_PREMIOS)
schedule.every().day.at("13:55:00").do(FLORIDA_AM_PREMIOS)
schedule.every().day.at("14:15:00").do(LOTEDOM_PREMIOS)
schedule.every().day.at("14:45:00").do(NEW_YORK_AM_PREMIOS)
schedule.every().day.at("14:50:00").do(Ganams_PREMIOS)
schedule.every().day.at("18:15:00").do(ANGUILA_TARDE_PREMIOS)
schedule.every().day.at("20:15:00").do(LOTEKA_PREMIOS)
schedule.every().day.at("20:20:00").do(PRIMERA_PM_PREMIOS)
schedule.every().day.at("21:16:00").do(LOTERIA_NACIONAL_PREMIOS)
schedule.every().day.at("21:16:00").do(LEIDSA_PREMIOS)
schedule.every().day.at("21:15:00").do(ANGUILA_NOCHE)
schedule.every().day.at("22:00:00").do(FLORIDA_PM_PREMIOS)
schedule.every().day.at("22:45:00").do(New_York_PM_Premios)

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