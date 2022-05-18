import os
from datetime import datetime
import platform
import requests
import json
from TOKEN_API_PRO_DE import API_KEY_MONGO_DB
#!----------------------------------------------------------------------
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_TARDE_TODO
from DATOS_LOTERIAS.Datos_NY_NOCHE import NEW_TORK_NOCHE_TODO
from DATOS_LOTERIAS.Datos_NY_TARDE import NEW_YORK_TARDE_TODO
from DATOS_LOTERIAS.DATOS_ANGUILA import ANGUILA_LOTTERY_TODO
from DATOS_LOTERIAS.Datos_Real import LOTO_REAL_TODO
from DATOS_LOTERIAS.Datos_Ganamas import LOTTERY_GANAMAS_TODO
from DATOS_LOTERIAS.Datos_Nacional_Noche import LOTTERY_NACIONAL_TODO
from DATOS_LOTERIAS.Datos_Loteka import LOTTERY_LOTEKA_TODO
from DATOS_LOTERIAS.Datos_Leidsa import LOTTERY_LEIDSA_TODO
from DATOS_LOTERIAS.Datos_La_suerte import LOTTERY_LA_SUERTE_TODO
from DATOS_LOTERIAS.Datos_La_Primera_AM import LOTTERY_LA_PRIMERA_AM
from DATOS_LOTERIAS.Datos_La_Primera_PM import LOTTERY_LA_PRIMERA_PM
from DATOS_LOTERIAS.Datos_Lotedom import LOTTERY_LOTEDOM_TODO
from DATOS_LOTERIAS.Datos_King_Lotery_MD_Y_PM import LOTTERY_KING_LOTTERY_MD_TODO, LOTTERY_KING_LOTTERY_PM_TODO
#!----------------------------------------------------------------------
mesesDic = {
    "01":'Enero',
    "02":'Febrero',
    "03":'Marzo',
    "04":'Abril',
    "05":'Mayo',
    "06":'Junio',
    "07":'Julio',
    "08":'Agosto',
    "09":'Septiembre',
    "10":'Octubre',
    "11":'Noviembre',
    "12":'Diciembre'
}

diasSemanaEso = {
    'Monday' : 'LUNES',
    'Tuesday' : 'MARTES',
    'Wednesday' : 'MIÉRCOLES',
    'Thursday' : 'JUEVES',
    'Friday' : 'VIERNES',
    'Saturday' : 'SÁBADO',
    'Sunday' : 'DOMINGO'
}


def comprobar_sistema():
    return platform.system()

def fecha(tipo_fecha):
    return datetime.today().strftime(tipo_fecha)

def Validar_Fecha_Hoy(fecha_comprobar):

    ANGUILA_MANANA = 'Draw 10:00AM. '+fecha('%d/%m/%Y')
    ANGUILA_MEDIO_DIA = 'Draw 1:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_TARDE = 'Draw 6:00PM. '+fecha('%d/%m/%Y')
    ANGUILA_NOCHE = 'Draw 9:00PM. '+fecha('%d/%m/%Y')
    mes_espanol=mesesDic[fecha('%m')]
    dia_espanol=diasSemanaEso[fecha('%A')]
    fecha_dia_un_digito = fecha('%d')
    fecha_dia_un_digito=fecha_dia_un_digito.lstrip('0')

    Todas_las_Fechas = [

    fecha('%A, %b %d, %Y'),
    fecha(f'%A, %b {fecha_dia_un_digito}, %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}th %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}st %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}nd %Y'),
    fecha(f'%A %B {fecha_dia_un_digito}rd %Y'),
    fecha('%A %B %dth %Y'),
    fecha('%a %m/%d/%y'),
    fecha('%A, %B %d, %Y'),
    fecha('%d-%m-%Y'),
    fecha('%d/%m/%Y'),
    fecha('%Y-%m-%d'),
    fecha(f'Sorteo: %d de {mes_espanol} del %Y.'),
    fecha(f'{dia_espanol}, %d-%m-%Y'),
    fecha('Resultados %d/%m/%Y'),
    ANGUILA_MANANA,
    ANGUILA_MEDIO_DIA,
    ANGUILA_TARDE,
    ANGUILA_NOCHE
    ]
    if fecha_comprobar in Todas_las_Fechas:
        return True
    else:
        #! AQUI TENGO QUE DEVOLVER FALSO ES UNA PRUEBA
        return False

def borrarPantalla():
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def Imprimir_Comandos(arreglo):
    ok = ''
    for i in arreglo:
        ok+=f"\n\n{i}"
    return ok

def solo_Numero(numero):
    if(len(numero)>=2):
        numero=numero[len(numero)-2:]
        caracteres = ['1','2','3','4','5','6','7','8','9','0']
        newNumero = ""
        for i in numero:
            if(i in caracteres):
                newNumero+=i
        return newNumero
    else:
        return numero

def solo_undigito(numero):
    numero=solo_Numero(numero)
    if(len(numero) == 1):
        return f'0{numero}'
    else:
        return numero

def saberLoteria(lote):
    if(lote == 'NEW YORK AM'):
        return NEW_YORK_TARDE_TODO
    elif(lote == 'NEW YORK PM'):
        return NEW_TORK_NOCHE_TODO
    elif(lote == 'FLORIDA AM'):
        return FLORIDA_TARDE_TODO
    elif(lote == 'FLORIDA PM'):
        return FLORIDA_NOCHE_TODO
    elif(lote == 'LOTERIA QUIN-PALE-TRIP 1:00 PM'):
        return LOTO_REAL_TODO
    elif(lote == 'GANAMAS'):
        return LOTTERY_GANAMAS_TODO
    elif(lote == 'LOTERIA NACIONAL'):
        return LOTTERY_NACIONAL_TODO
    elif(lote =='LOTEKA'):
        return LOTTERY_LOTEKA_TODO
    elif(lote == 'QTP-9PM'):
        return LOTTERY_LEIDSA_TODO
    elif(lote == 'La Suerte'):
        return LOTTERY_LA_SUERTE_TODO
    elif(lote == '12M AM'):
        return LOTTERY_LA_PRIMERA_AM
    elif(lote == '12M PM'):
        return LOTTERY_LA_PRIMERA_PM
    elif(lote == 'Lotedom'):
        return LOTTERY_LOTEDOM_TODO
    elif(lote == 'Anguila MD' or lote == 'Anguila AM' or lote == 'Anguila Tarde' or lote == 'Anguila Noche'):
        return ANGUILA_LOTTERY_TODO
    elif(lote == 'King Lottery Medio Dia'):
        return LOTTERY_KING_LOTTERY_MD_TODO
    elif(lote == 'King Lottery Noche'):
        return LOTTERY_KING_LOTTERY_PM_TODO
    else:
        return False

def saber_Nombre_Loteria_Sorteo(lote):
    if(lote == '/Obtener_New_York_AM' or lote == '/Premiar_New_York_AM'):
        return ['New York', 'NEW YORK AM']

    elif(lote == '/Obtener_New_York_PM' or lote == '/Premiar_New_York_PM'):
        return ['New York', 'NEW YORK PM']

    elif(lote == '/Obtener_Florida_AM' or lote == '/Premiar_Florida_AM'):
        return ['Florida', 'FLORIDA AM']

    elif(lote == '/Obtener_Florida_PM' or lote == '/Premiar_Florida_PM'):
        return ['Florida', 'FLORIDA PM']

    elif(lote == '/Obtener_Loteria_Real' or lote == '/Premiar_Loteria_Real'):
        return ['REAL', 'LOTERIA QUIN-PALE-TRIP 1:00 PM']

    elif(lote == '/Obtener_Loteria_Ganamas' or lote == '/Premiar_Loteria_Ganamas'):
        return ['GANAMAS', 'GANAMAS']

    elif(lote == '/Obtener_Loteria_Nacional' or lote == '/Premiar_Loteria_Nacional'):
        return ['NACIONAL','LOTERIA NACIONAL']

    elif(lote == '/Obtener_Loteria_Loteka' or lote == '/Premiar_Loteria_Loteka'):
        return ['LOTERIA 7 PM', 'LOTEKA']

    elif(lote == '/Obtener_Loteria_Leidsa' or lote == '/Premiar_Loteria_Leidsa'):
        return ['LOTERIA 9 PM', 'QTP-9PM']

    elif(lote == '/Obtener_Loteria_La_Suerte' or lote == '/Premiar_Loteria_La_Suerte'):
        return ['La Suerte','La Suerte']

    elif(lote == '/Obtener_Loteria_La_Primera_AM' or lote == '/Premiar_Loteria_La_Primera_AM' ):
        return ['12M', '12M AM']

    elif (lote == '/Obtener_Loteria_La_Primera_PM' or lote == '/Premiar_Loteria_La_Primera_PM'):
        return ['12M', '12M PM']

    elif(lote == '/Obtener_Anguila_AM' or lote == '/Premiar_Anguila_AM'):
        return ['Anguila', 'Anguila AM']

    elif(lote == '/Obtener_Anguila_MD' or lote == '/Premiar_Anguila_MD'):
        return ['Anguila', 'Anguila MD']

    elif(lote == '/Obtener_Anguila_Tarde' or lote == '/Premiar_Anguila_TARDE'):
        return ['Anguila', 'Anguila Tarde' ]

    elif(lote == '/Obtener_Anguila_PM' or lote == '/Premiar_Anguila_NOCHE'):
        return ['Anguila', 'Anguila Noche']

    elif(lote == '/Obtener_Lotedom' or lote == '/Premiar_Lotedom'):
        return ['Lotedom','Lotedom']

    elif(lote == '/Obtener_King_Lottery_AM'):
        return ['King Lottery','King Lottery Medio Dia']

    elif(lote == '/Obtener_King_Lottery_PM'):
        return ['King Lottery','King Lottery Noche']

    else:
        return False


def Saber_Loteria_Seleccionada(inputLoteria,sorteo):
    inputLoteria=inputLoteria.lower()
    return inputLoteria.endswith(sorteo.lower())

def Peticion_GET(sorteo,fecha):
    try:
        url = f'http://localhost:9000/api/sorteo/{sorteo}/{fecha}'
        r=requests.get(url)
        if(r.status_code == 200):
            if(r.text != 'null'):
                return r.json()
            else:
                return 'Los numeros no fueron encontrados en La Base de Datos'
        else:
            return 'El SERVIDOR no respondio'
    except:
        return('HUBO UN ERRORRRRRRR al Momento de la Petcion GET' )

def imprimir_resultados(json):
    if(type(json)==dict):
        loteria = json['loteria']
        sorteo = json['sorteo']
        mumeros_ganadores=json['numeros_ganadores']
        if(loteria and sorteo and len(mumeros_ganadores) == 3):
            numero_1 = mumeros_ganadores[0]
            numero_2 = mumeros_ganadores[1]
            numero_3 = mumeros_ganadores[2]
            return  f'Loteria: {loteria}\nSorteo: {sorteo}\nNumeros Ganadores: {numero_1}-{numero_2}-{numero_3}\n'
        else:
            json
    else:
        return json

def Obtener_User_MONGO_NOTIFICACIONES():
    url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/beta/action/find"
    payload = json.dumps({
        "collection": "Usuarios_Notificaciones",
        "database": "myFirstDatabase",
        "dataSource": "LoteriasCluster",
        "projection": {

        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY_MONGO_DB
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    arr=response.json()

    New_Arr = []
    for user in arr['documents']:
        usuarios = user['user_id']
        New_Arr.append(usuarios)
    return New_Arr

def Nuevos_Usuarios_Mongo_DB(user):
    url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/beta/action/findone"
    payload = json.dumps({
        "collection": "Usuarios_Notificaciones",
        "database": "myFirstDatabase",
        "dataSource": "LoteriasCluster",
        "projection": {
            'user_id': user
        }
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY_MONGO_DB
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    arr=response.json()

def Verificar_si_un_usuario_existe(user):
    url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/beta/action/findOne"
    payload = json.dumps({
        "collection": "Usuarios_Notificaciones",
        "database": "myFirstDatabase",
        "dataSource": "LoteriasCluster",
        "filter": { 'user_id': user}
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY_MONGO_DB
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    respuesta=(response.json())
    if(respuesta['document']==None):
        print("\n\n\nAgregando nuevo Usuaio a la BD\n\n\n")
        return True
    else:
        print("\n\n\nEste Usuario ya existe en la Base de Dato\n\n\n")
        return False

def Agregar_Nuevo_Usuario_MONGODB(user):
    url = "https://data.mongodb-api.com/app/data-rrmjk/endpoint/data/beta/action/insertOne"
    payload = json.dumps({
        "collection": "Usuarios_Notificaciones",
        "database": "myFirstDatabase",
        "dataSource": "LoteriasCluster",
        "document": { 'user_id': user}
    })
    headers = {
        'Content-Type': 'application/json',
        'Access-Control-Request-Headers': '*',
        'api-key': API_KEY_MONGO_DB
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    respuesta=(response.json())
    return respuesta