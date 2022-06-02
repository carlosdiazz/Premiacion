from pickle import FALSE
import schedule
from Funciones_Necesarias import fecha, borrarPantalla, saber_Nombre_Loteria_Sorteo, Peticion_GET
import time
from ORKAPI import ORKAPI
#from Funciones_para_buscar_premios import sendNotification


class Premiar_Loterias_():

    def __init__(self, loteriaARG):
        self.loteria = loteriaARG
        self.intentos = 0

    def Premiar_Loterias(self):

        if(self.intentos <= 40) :
            self.intentos = self.intentos + 1
            print('Inicio el Proceso de Premiacion')
            loteria_selecionada = self.loteria
            Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteria_selecionada)
            self.nombre_loteria = Nombre_loteria_sorteo[0]
            self.nombre_sorteo = Nombre_loteria_sorteo[1]
            fecha_AHORA = fecha('%d-%m-%Y')
            #! ---------------------------------------------------------------------
            peticion_GET = Peticion_GET(self.nombre_sorteo,fecha_AHORA)

            if(type(peticion_GET)==dict):
                numeros_a_publicar = peticion_GET['numeros_ganadores']
                result = ORKAPI(self.nombre_loteria,self.nombre_sorteo,numeros_a_publicar)
                if(result[0]):
                    print('SE PUBLICO BIEN')
                    return ''
                else:
                    print('SOGIUE INTENTANDO NO SE PUBLICO')
                    time.sleep(30)
                    self.Premiar_Loterias()
            else:
                print(peticion_GET)
                time.sleep(30)
                self.Premiar_Loterias()




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