import os, time
from datetime import datetime
import platform


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