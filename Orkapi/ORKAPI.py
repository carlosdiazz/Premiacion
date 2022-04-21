from API_Numeros_Americanos import  borrarPantalla
from ColocarPremio import Colocar_Numeros_Plataforma
from PROCESO import PROCESO
import time

url = 'https://dev_admin.orkapi.net/'
username = 'carlos@premio'
password = 1234

def ORKAPI(loteria, horario):

    numeros_a_publicar=PROCESO(loteria,horario)
    if(numeros_a_publicar):
        borrarPantalla()
        print("Los numeros han sido confirmados y son Correctos")
        print("Los numeros que se van a publicar son")
        print(numeros_a_publicar)
        time.sleep(1)
        comprobar=Colocar_Numeros_Plataforma(url, username, password, loteria,horario, numeros_a_publicar).resultado_final()
        if(comprobar):
            print('Numero Publicado')
            return numeros_a_publicar
        else:
            print("Numeros ya estan Publicados")
            return 'Numeros han sido Publicados'

    else:
        print("No se publicaron los Numeros")
        return False
