
from Funciones_Necesarias import fecha, saber_Nombre_Loteria_Sorteo, Peticion_GET, Obtener_User_MONGO_NOTIFICACIONES, Saber_Loteria_Especifo_Por_Plataformas, Saber_Sorteo_Especifo_Por_Plataformas
import time
from ORKAPI import ORKAPI
import requests

#! Aqui creo mi clase que es para poder premiar Automatico Las Diferentes Plataformas

def sendNotification(message,token ):
    try:
        bot_token = token
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

    def __init__(self, loteriaARG, plataforma):
        self.Nombre_loteria_sorteo = saber_Nombre_Loteria_Sorteo(loteriaARG)
        self.intentos = 0
        nombre_loteria = self.Nombre_loteria_sorteo[0]
        nombre_Sorteo = self.Nombre_loteria_sorteo[1]
        #print(f'Inicio el Proceso de Premiacion Loteria: {nombre_loteria} Sorteo: {nombre_Sorteo}')
        self.respuesta = f'\n\nCOMENZO EL PROCESO PARA PREMIAR EN PLATAFORMA PARA LA LOTERIA: {nombre_loteria} CON EL SORTEO {nombre_Sorteo}\n\n'
        self.token = plataforma['token']
        self.url = plataforma['url']
        self.username = plataforma['username']
        self.password = plataforma['password']
        self.plataforma = plataforma['plataforma']

    def Premiar_Loterias(self):

        nombre_loteria = self.Nombre_loteria_sorteo[0]
        nombre_Sorteo = self.Nombre_loteria_sorteo[1]
        url=self.url
        username=self.username
        password=self.password
        token=self.token
        plataforma=self.plataforma

        Nombre_Loteria_Plataforma = Saber_Loteria_Especifo_Por_Plataformas (nombre_loteria,plataforma) #! Esta mandare a Orkapi
        Nombre_Sorteo_Plataforma = Saber_Sorteo_Especifo_Por_Plataformas (nombre_Sorteo,plataforma) #! Esta mandare a Orkapi

        fecha_ahorAA = fecha('%d-%m-%Y')
        peticion = Peticion_GET(nombre_Sorteo,fecha_ahorAA)

        if(self.intentos <= 150) :
            self.intentos = self.intentos + 1

            if(type(peticion) == dict):
                numeros_a_publicar = peticion['numeros_ganadores']
                result = ORKAPI(Nombre_Loteria_Plataforma,Nombre_Sorteo_Plataforma,numeros_a_publicar,url,username,password)
                if(result[0]):
                    print(f'INTENTO #{self.intentos}')
                    print(f'SE PUBLICO BIEN ----> {result[1]}')
                    self.respuesta = result[1]
                    self.intentos=200
                    self.Premiar_Loterias()

                else:
                    print(f'\n\nINTENTO #{self.intentos}\n\n')
                    print(f'\n\nSIGUE INTENTANDO NO SE PUBLICO ----> {result[1]}')
                    time.sleep(20)
                    self.respuesta = result[1]
                    self.Premiar_Loterias()
            else:
                print(f'\n\nINTENTO #{self.intentos}\n\n')
                print(f'\n\nERROR --> PREMIAR PLATAFORMA --> LOTERIA: {Nombre_Loteria_Plataforma} Sorteo: {nombre_Sorteo} ---> {peticion}\n\n')
                time.sleep(20)
                self.respuesta = peticion
                self.Premiar_Loterias()
        else:
            print(f'\n\nPREMIAR PLATAFORMA: {plataforma}\n\n\n--> LOTERIA: {nombre_loteria}\n--> Sorteo: {Nombre_Sorteo_Plataforma}\n\n\n--> {self.respuesta}\n\n' )
            sendNotification(f'\n\nPREMIACION PLATAFORMA: {plataforma} \n\n\n--> LOTERIA: {Nombre_Loteria_Plataforma}\n--> Sorteo: {Nombre_Sorteo_Plataforma}\n\n\n--> {self.respuesta}',token )
            self.intentos=0