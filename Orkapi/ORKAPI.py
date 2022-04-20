from API_Numeros_Americanos import  borrarPantalla
from ColocarPremio import Premio
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
        time.sleep(5)
        Premio(url, username, password, loteria, numeros_a_publicar, horario)
        print('Numero Publicado')
        return numeros_a_publicar

    else:
        print("No se publicaron los Numeros")
        return False


ORKAPI('New York',"PM")

#main(True,'New York','AM')
#main(True,'New York','PM')
#main(True,'Florida', 'AM')
#main(True, 'Florida', 'PM')
#print(main(True,'New York','AM').prueeee)