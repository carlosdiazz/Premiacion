import schedule
import time
from Doble_Check import Doble_Check
from Funciones_Necesarias import saberLoteria, fecha, saber_Nombre_Loteria_Sorteo, Obtener_User_MONGO_NOTIFICACIONES, borrarPantalla
import requests
import json
from Enviar_Correo import Enviar_Corre
from os import remove
from TOKEN_API_PRO_DE import TOKEN_NOTIFICACION

def sendNotification(VALIDAR,message ):
    try:
        mess=''
        if(VALIDAR):
            mess='SE ACABA DE PUBLICAR LA SIGUINTE INFORMACION\n\n'
            for mensaje in message:
                mess=mess+str(mensaje)+" \n"
        else:
            mess = message
        bot_token = TOKEN_NOTIFICACION
        User=Obtener_User_MONGO_NOTIFICACIONES()
        for usuarios in User:
            send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + usuarios + '&parse_mode=Markdown&text=' + mess
            requests.get(send_text)
            requests.post(f'https://api.telegram.org/bot{bot_token}/sendPhoto',
                files={'photo': ('./LOTERIA_PAGES.png', open('./LOTERIA_PAGES.png', 'rb'))},
                data={'chat_id': usuarios, 'caption': 'Loteria'})
    except:
        print('-----------------------------------------------------------------------')
        print("NO SE PUEDO ENVIAR LA NOTIFICACION DE TELEGRAM O LA FOTO NO SE ENCONTRO")
        print('-----------------------------------------------------------------------')
        time.sleep(60)

def Peticion_POST(Loteria):
    try:
        headers = { 'Content-Type': 'application/json'}
        url = 'http://localhost:9000/api/sorteo'
        body2= json.dumps({
            "loteria": Loteria[0],
            "sorteo":Loteria[1],
            'numeros_ganadores':Loteria[2],
            "fecha" : Loteria[3],
            "agregado_por": Loteria[4]
        })
        Peticion_POST=requests.post(url, headers=headers, data= body2)
        if(Peticion_POST.status_code == 200):
            return True
        else:
            return False
    except:
        print(f'\n\n\nNO SE PREMIO ESTA LOTERIA: {Loteria[0]} CON ESTE SORTEO {Loteria[1]} -------> El SERVIDOR EXPRES NO RESPONDE' )
        return False

def VALIDAR_QUE_NO_EXISTAN(sorteo,fecha):
    try:
        url = f'http://localhost:9000/api/sorteo/{sorteo}/{fecha}'
        r=requests.get(url)
        if(r.status_code == 200):
            if(r.text == 'null'):
                return True
            else:
                return 'Los Numeros ya estan Publicado'
        else:
            return 'El SERVIDOR no respondio'
    except:
        return('HUBO UN ERRORRRRRRR al Momento de la Petcion GET' )

class Buscar():

    def __init__(self,lotery):
        self.lotery=lotery
        self.intentos=0

    def Buscar_Loteria(self):
        lotery = self.lotery
        Loteria_Y_Sorteo = saber_Nombre_Loteria_Sorteo(lotery)
        loteria = Loteria_Y_Sorteo[0]
        sorteo = Loteria_Y_Sorteo[1]
        fecha_hoy = fecha('%d-%m-%Y')
        validar = VALIDAR_QUE_NO_EXISTAN(sorteo,fecha_hoy)
        if(validar==True):
            print(f'\n\nBuscando la loteria: {loteria} con el sorteo: {sorteo} \n\n')
            lotery_ARREGLO = saberLoteria(sorteo)
            numeros_Ganadores = Doble_Check(lotery_ARREGLO)

            if(numeros_Ganadores):
                if(numeros_Ganadores[0].startswith('Anguila')):
                    if(numeros_Ganadores[0]==sorteo):
                        numeros_Ganadores=numeros_Ganadores[1:]
                    else:
                        numeros_Ganadores=False
                        remove('./LOTERIA_PAGES.png')
                else:
                    pass

            if(numeros_Ganadores):

                print(f'-------------------------------> {numeros_Ganadores} \n\n')
                Arreglo_loteria=[
                    loteria,
                    sorteo,
                    numeros_Ganadores,
                    fecha_hoy,
                    'Bot'
                ]
                if(Peticion_POST(Arreglo_loteria) == True):
                    print(f'\n\nSe Publico esta loteria: {loteria} con este sorteo: {sorteo} en la base de Datos. \n\n')
                    sendNotification(True,Arreglo_loteria)
                    Enviar_Corre(Arreglo_loteria)
                    remove('./LOTERIA_PAGES.png')
                    return True
                else:
                    print(f'\n\nNo se publico esta Loteria: {loteria}, con este sorteo: {sorteo} en la base de Datos -------> El SERVIDOR EXPRES NO RESPONDE\n\n')
                    sendNotification(False,f'No se publico esta Loteria: {loteria}, con este sorteo: {sorteo}  en la base de Datos-------> El SERVIDOR EXPRES NO RESPONDE')
                    return False

            else:
                self.intentos = self.intentos+1
                intentos = self.intentos
                if(self.intentos <= 30):
                    print(f"\n\n\nNo se encontro esta loteria {loteria} con este sorteo: {sorteo}---------------------> Intento #{intentos}")
                    time.sleep(60)
                    self.Buscar_Loteria()


                else:
                    sendNotification(False,f'No se publico esta loteria: {loteria} con este sorteo: {sorteo}, en la Base De Datos \n\nSe intento {intentos} veces')
                    try:
                        remove('./LOTERIA_PAGES.png')
                    except:
                        pass
                    print(f'\n\nNo se premio esta loteria: {loteria} con este sorteo: {sorteo}, se intento {intentos} veces \n\n')
                    return False
        else:
            print('---------------------------------------------------')
            print(validar)
            print(f'Para la loteria: {loteria} con el sorteo: {sorteo}.')
            print('---------------------------------------------------')
            sendNotification(False,f'No se publico esta Loteria: {loteria}, con este sorteo: {sorteo} --->  {validar}')

#! ----------------------------------------------------------
La_Primera_AM = Buscar('/Obtener_Loteria_La_Primera_AM').Buscar_Loteria
La_Suerte = Buscar('/Obtener_Loteria_La_Suerte').Buscar_Loteria
Real = Buscar('/Obtener_Loteria_Real').Buscar_Loteria
Lotedom = Buscar('/Obtener_Lotedom').Buscar_Loteria
Florida_AM = Buscar('/Obtener_Florida_AM').Buscar_Loteria
New_York_AM = Buscar('/Obtener_New_York_AM').Buscar_Loteria
Ganamas = Buscar('/Obtener_Loteria_Ganamas').Buscar_Loteria
Loteka = Buscar('/Obtener_Loteria_Loteka').Buscar_Loteria
La_Primera_PM = Buscar('/Obtener_Loteria_La_Primera_PM').Buscar_Loteria
Leidsa = Buscar('/Obtener_Loteria_Leidsa').Buscar_Loteria
Loteria_Nacional = Buscar('/Obtener_Loteria_Nacional').Buscar_Loteria
New_York_PM = Buscar('/Obtener_New_York_PM').Buscar_Loteria
Florida_PM = Buscar('/Obtener_Florida_PM').Buscar_Loteria
King_Lottery_MD = Buscar('/Obtener_King_Lottery_AM').Buscar_Loteria
King_Lottery_PM = Buscar('/Obtener_King_Lottery_PM').Buscar_Loteria
#? ---------------------------------------------------------
Anguila_AM = Buscar('/Obtener_Anguila_AM').Buscar_Loteria
Anguila_MD = Buscar('/Obtener_Anguila_MD').Buscar_Loteria
Anguila_TARDE = Buscar('/Obtener_Anguila_Tarde').Buscar_Loteria
Anguila_PM = Buscar('/Obtener_Anguila_PM').Buscar_Loteria
#! ---------------------------------------------------------
schedule.every().day.at("10:10:00").do(Anguila_AM)
schedule.every().day.at("12:10:00").do(La_Primera_AM)
schedule.every().day.at("12:40:00").do(La_Suerte)
schedule.every().day.at("12:50:00").do(King_Lottery_MD)
schedule.every().day.at("13:10:00").do(Real)
schedule.every().day.at("13:15:00").do(Anguila_MD)
schedule.every().day.at("14:00:00").do(Florida_AM)
schedule.every().day.at("14:10:00").do(Lotedom)
schedule.every().day.at("14:40:00").do(New_York_AM)
schedule.every().day.at("14:50:00").do(Ganamas)
schedule.every().day.at("18:10:00").do(Anguila_TARDE)
schedule.every().day.at("19:45:00").do(King_Lottery_PM)
schedule.every().day.at("20:10:00").do(Loteka)
schedule.every().day.at("20:10:00").do(La_Primera_PM)
schedule.every().day.at("21:10:00").do(Leidsa)
schedule.every().day.at("21:10:00").do(Loteria_Nacional)
schedule.every().day.at("21:15:00").do(Anguila_PM)
schedule.every().day.at("22:10:00").do(Florida_PM)
schedule.every().day.at("22:50:00").do(New_York_PM)


borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(60)