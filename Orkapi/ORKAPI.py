from API_CONSULTAS import Obtener, borrarPantalla
from ColocarPremio import Premio
from Datos_Loterias import NEW_YORK_TARDE_LOTTERY, NEW_YORK_TARDE_LOTTERYUSA, NEW_YORk_TARDE_OFICIAL_NUMBERS

url = 'https://dev_admin.orkapi.net/'

class main():

    def __init__(self):
        NY_tarde_URL_1 = Obtener(True, NEW_YORK_TARDE_LOTTERY).devolver_numeros()
        NY_tarde_URL_2 = Obtener(True, NEW_YORK_TARDE_LOTTERYUSA).devolver_numeros()
        NY_tarde_URL_3 = Obtener(True,NEW_YORk_TARDE_OFICIAL_NUMBERS).devolver_numeros()

        if(NY_tarde_URL_1 == NY_tarde_URL_2 == NY_tarde_URL_3):
            print("LOS NUMEROS SON IGUALES")
            Premio(url, 'carlos@premio',1234,'NEW YORK',NY_tarde_URL_1, 'AM' )
            borrarPantalla()
            print(f'NUMEROS PUBLICADOS...')
        else:
            print('Los Numeros Son Diferentes')
main()