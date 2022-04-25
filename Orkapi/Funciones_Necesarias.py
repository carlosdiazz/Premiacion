import os, time
from datetime import datetime
import platform
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

    Todas_las_Fechas = [
        fecha('%A, %b %d, %Y'),
        fecha('%A %B %dth %Y'),
        fecha('%a %m/%d/%y'),
        fecha('%A, %B %d, %Y'),
        fecha('%d-%m-%Y'),
        fecha('%d/%m/%Y'),
        fecha(f'Sorteo: %d de {mes_espanol} del %Y.'),
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
    if(lote == 'New York AM'):
        return NEW_YORK_TARDE_TODO
    elif(lote == 'New York PM'):
        return NEW_TORK_NOCHE_TODO
    elif(lote == 'Florida AM'):
        return FLORIDA_TARDE_TODO
    elif(lote == 'FLorida PM'):
        return FLORIDA_NOCHE_TODO
    elif(lote == 'Loteria REAL'):
        return LOTO_REAL_TODO
    elif(lote == 'Ganamas'):
        return LOTTERY_GANAMAS_TODO
    elif(lote == 'Nacional'):
        return LOTTERY_NACIONAL_TODO
    elif(lote =='Loteka'):
        return LOTTERY_LOTEKA_TODO
    elif(lote == 'Leidsa'):
        return LOTTERY_LEIDSA_TODO
    elif(lote == 'La Suerte'):
        return LOTTERY_LA_SUERTE_TODO
    elif(lote == 'Anguila MD' or lote == 'Anguila AM' or lote == 'Anguila Tarde' or lote == 'Anguila PM'):
        return ANGUILA_LOTTERY_TODO
    else:
        return False

def saberNombreLoteria(lote):
    if(lote == '/Obtener_New_York_AM' or lote == '/Premiar_New_York_AM'):
        return 'New York AM'
    elif(lote == '/Obtener_New_York_PM' or lote == '/Premiar_New_York_PM'):
        return 'New York PM'
    elif(lote == '/Obtener_Florida_AM' or lote == '/Premiar_Florida_AM'):
        return 'Florida AM'
    elif(lote == '/Obtener_Florida_PM' or lote == '/Premiar_Florida_PM'):
        return 'FLorida PM'
    elif(lote == '/Obtener_Loteria_Real' or lote == '/Premiar_Loteria_Real'):
        return 'Loteria REAL'
    elif(lote == '/Obtener_Loteria_Ganamas'):
        return 'Ganamas'
    elif(lote == '/Obtener_Loteria_Nacional'):
        return 'Nacional'
    elif(lote == '/Obtener_Loteria_Loteka'):
        return 'Loteka'
    elif(lote == '/Obtener_Loteria_Leidsa'):
        return 'Leidsa'
    elif(lote == '/Obtener_Loteria_La_Suerte' or lote == '/Premiar_Loteria_La_Suerte'):
        return 'La Suerte'
    elif(lote == '/Obtener_Anguila_AM'):
        return 'Anguila AM'
    elif(lote == '/Obtener_Anguila_MD' ):
        return 'Anguila MD'
    elif('/Obtener_Anguila_Tarde'):
        return 'Anguila Tarde'
    elif('/Obtener_Anguila_PM'):
        return 'Anguila PM'

    else:
        return False

def Saber_loteria_Plataforma(message):

    if(message == 'New York PM' ):
        return ['New York', 'NEW YORK PM ']

    elif(message == 'New York AM' ):
        return ['New York', 'NEW YORK AM ']

    elif(message == 'FLorida PM' ):
        return ['Florida', 'FLORIDA PM ']

    elif(message == 'Florida AM' ):
        return ['Florida', 'FLORIDA AM ']

    elif(message == 'Loteria REAL'):
        return ['REAL', 'LOTERIA QUIN-PALE-TRIP 1:00 PM ']

    elif(message == 'La Suerte'):
        return ['La Suerte','La Suerte']

def saber_si_loteria_es_anguila(numeros):
    fecha_de_hoy = fecha('%d/%m/%Y')
    if(numeros[0] == 'Draw 10:00AM. '+fecha_de_hoy):
        return 'Anguila AM'
    elif(numeros[0] == 'Draw 1:00PM. '+fecha_de_hoy):
        return 'Anguila MD'
    elif(numeros[0] == 'Draw 5:00PM. '+fecha_de_hoy):
        return 'Anguila Tarde'
    elif(numeros[0] == 'Draw 9:00PM. '+fecha_de_hoy):
        return 'Anguila PM'
    else:
        return False