import schedule
import time
from Doble_Check import Doble_Check
from Funciones_Necesarias import saberLoteria, fecha, saber_Nombre_Loteria_Sorteo
import requests
import json
from Enviar_Correo import Enviar_Corre
from os import remove

def Peticion_POST(Loteria):
    try:
        headers = { 'Content-Type': 'application/json'}
        url = 'http://localhost:9000/api/sorteo'
        body2= json.dumps({
            "loteria": Loteria[0],
            "sorteo":Loteria[1],
            'numeros_ganadores':Loteria[2],
            "fecha" : Loteria[3]
        })
        requests.post(url, headers=headers, data= body2)
    except:
        print(f'NO SE PREMIO ESTA LOTERIA: {Loteria[0]} CON ESTE SORTEO {Loteria[1]}' )

class Buscar():

    def __init__(self,lotery):
        self.lotery=lotery

    def Buscar_Loteria(self):
        lotery = self.lotery
        Loteria_Y_Sorteo = saber_Nombre_Loteria_Sorteo(lotery)
        loteria = Loteria_Y_Sorteo[0]
        sorteo =Loteria_Y_Sorteo[1]

        lotery_ARREGLO = saberLoteria(sorteo)
        numeros_Ganadores = Doble_Check(lotery_ARREGLO)

        if(numeros_Ganadores):
            loteria=[
                loteria,
                sorteo,
                numeros_Ganadores,
                fecha('%d-%m-%Y')
            ]
            #! CONTROLAR EL ERROR SI NO SE ENVIA EL CORREO
            Peticion_POST(loteria)
            Enviar_Corre(loteria)
            remove('./LOTERIA_PAGES.png')

        else:
            time.sleep(300)
            self.Buscar_Loteria()



#! ----------------------------------------------------------
La_Primera_AM = Buscar('/Obtener_Loteria_La_Primera_AM').Buscar_Loteria
La_Suerte = Buscar('/Obtener_Loteria_La_Suerte').Buscar_Loteria
Real = Buscar('/Obtener_Loteria_Real').Buscar_Loteria
Florida_AM = Buscar('/Obtener_Florida_AM').Buscar_Loteria
New_York_AM = Buscar('/Obtener_New_York_AM').Buscar_Loteria
Ganamas = Buscar('/Obtener_Loteria_Ganamas').Buscar_Loteria
Loteka = Buscar('/Obtener_Loteria_Loteka').Buscar_Loteria
La_Primera_PM = Buscar('/Obtener_Loteria_La_Primera_PM').Buscar_Loteria
Leidsa = Buscar('/Obtener_Loteria_Leidsa').Buscar_Loteria
Loteria_Nacional = Buscar('/Obtener_Loteria_Nacional').Buscar_Loteria
New_York_PM = Buscar('/Obtener_New_York_PM').Buscar_Loteria
Florida_PM = Buscar('/Obtener_Florida_PM').Buscar_Loteria
#! ---------------------------------------------------------

schedule.every().day.at("12:10:00").do(La_Primera_AM)
schedule.every().day.at("12:40:00").do(La_Suerte)
schedule.every().day.at("13:10:00").do(Real)
schedule.every().day.at("14:00:00").do(Florida_AM)
schedule.every().day.at("14:50:00").do(New_York_AM)
schedule.every().day.at("15:10:00").do(Ganamas)
schedule.every().day.at("20:10:00").do(Loteka)
schedule.every().day.at("20:10:00").do(La_Primera_PM)
schedule.every().day.at("21:10:00").do(Leidsa)
schedule.every().day.at("21:10:00").do(Loteria_Nacional)
schedule.every().day.at("22:10:00").do(Florida_PM)
schedule.every().day.at("22:50:00").do(New_York_PM)



while True:
    fecha_actual = fecha('%d-%m-%Y %H:%M:%S')
    print(f"---------- {fecha_actual} ----------")
    schedule.run_pending()
    time.sleep(600)
