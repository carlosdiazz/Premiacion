from API_Numeros_Americanos import  borrarPantalla
from ColocarPremio import Colocar_Numeros_Plataforma
import time

url = 'https://dev_admin.orkapi.net/'
username = 'carlos@premio'
password = 1234

def ORKAPI(loteria, horario, numeros_a_publicar):

    print("Los numeros han sido confirmados y son Correctos")
    print("Los numeros que se van a publicar son")
    print(numeros_a_publicar)

    comprobar=Colocar_Numeros_Plataforma(url, username, password, loteria,horario, numeros_a_publicar).resultado_final()
    if(comprobar):
        print('Numero Publicado')
        return f'Numero Publicado {loteria} {numeros_a_publicar}'
    else:
        print("Numeros ya estan Publicados")
        return 'Esta Loteria ya esta premiada en Plataforma'
