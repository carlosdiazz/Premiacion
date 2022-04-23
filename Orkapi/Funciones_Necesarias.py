import os, time
from datetime import datetime
import platform
#!----------------------------------------------------------------------
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_TARDE_TODO
from DATOS_LOTERIAS.Datos_NY_NOCHE import NEW_TORK_NOCHE_TODO
from DATOS_LOTERIAS.Datos_NY_TARDE import NEW_YORK_TARDE_TODO
#!----------------------------------------------------------------------
def comprobar_sistema():
    return platform.system()

def fecha(tipo_fecha):
    return datetime.today().strftime(tipo_fecha)

def Validar_Fecha_Hoy(fecha_comprobar):

    Todas_las_Fechas = [
        fecha('%A, %b %d, %Y'),
        fecha('%A %B %dth %Y'),
        fecha('%a %m/%d/%y'),
        fecha('%A, %B %d, %Y'),
        fecha('%d-%m-%Y')
        ]
    if fecha_comprobar in Todas_las_Fechas:
        return True
    else:
        return False

def borrarPantalla():
    if os.name == "posix":
        time.sleep(1)
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")

def Imprimir_Comandos(arreglo):
    ok = ''
    for i in arreglo:
        ok+=f"\n\n{i}"
    return ok

def solo_undigito(numero):
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
