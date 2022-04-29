import schedule
import time
from Doble_Check import Doble_Check
from Funciones_Necesarias import saberLoteria, Saber_loteria_Plataforma, fecha
import requests
import json

def Peticion_POST(Loteria):
    try:
        headers = { 'Content-Type': 'application/json'}
        url = 'http://localhost:9000/api/loterias'
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
    def Buscar_Loteria(self):
        lotery = self.lotery
        lotery_ARREGLO = saberLoteria(lotery)
        numeros_Ganadores = Doble_Check(lotery_ARREGLO)

        if(numeros_Ganadores):
            arr_Plataforma = Saber_loteria_Plataforma(lotery)
            loteria=[
                arr_Plataforma[0],
                arr_Plataforma[1],
                numeros_Ganadores,
                fecha('%d-%m-%Y')
            ]
            Peticion_POST(loteria)

        else:
            self.Buscar_Loteria()
            time.sleep(300)

    def __init__(self,lotery):
        self.lotery=lotery
        pass

#! ----------------------------------------------------------
La_Primera_AM = Buscar('La Primera AM').Buscar_Loteria
La_Suerte = Buscar('La Suerte').Buscar_Loteria
Real = Buscar('Loteria REAL').Buscar_Loteria
Florida_AM = Buscar('Florida AM').Buscar_Loteria
New_York_AM = Buscar('New York AM').Buscar_Loteria
Ganamas = Buscar('Ganamas').Buscar_Loteria
Loteka = Buscar('Loteka').Buscar_Loteria
La_Primera_PM = Buscar('La Primera PM').Buscar_Loteria
Leidsa = Buscar('Leidsa').Buscar_Loteria
Loteria_Nacional = Buscar('Loteria Nacional').Buscar_Loteria
New_York_PM = Buscar('New York PM').Buscar_Loteria
Florida_PM = Buscar('FLorida PM').Buscar_Loteria
#! ---------------------------------------------------------

schedule.every().day.at("12:10:00").do(La_Primera_AM)
schedule.every().day.at("12:40:00").do(La_Suerte)
schedule.every().day.at("13:15:00").do(Real)
schedule.every().day.at("13:55:00").do(Florida_AM)
schedule.every().day.at("14:55:00").do(New_York_AM)
schedule.every().day.at("15:15:00").do(Ganamas)
schedule.every().day.at("20:10:00").do(Loteka)
schedule.every().day.at("20:15:00").do(La_Primera_PM)
schedule.every().day.at("21:15:00").do(Leidsa)
schedule.every().day.at("21:20:00").do(Loteria_Nacional)
schedule.every().day.at("21:55:00").do(Florida_PM)
schedule.every().day.at("22:50:00").do(New_York_PM)



while True:
    fecha_actual = fecha('%d-%m-%Y %H:%M:%S')
    print(f"--------------------- {fecha_actual} ----------------------")
    schedule.run_pending()
    time.sleep(600)
