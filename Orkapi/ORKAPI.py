from API_Numeros_Americanos import Obtener, borrarPantalla
from ColocarPremio import Premio
from DATOS_LOTERIAS.Datos_NY_TARDE import NEW_YORK_TARDE_TODO
from DATOS_LOTERIAS.Datos_NY_NOCHE import NEW_TORK_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_TARDE_TODO
url = 'https://dev_admin.orkapi.net/'

class main():

    def __init__(self,americana,loteria,sorteo):

        if(americana):
            if(loteria == 'New York' and sorteo == 'AM'):
                self.lote = NEW_YORK_TARDE_TODO
                self.premiar_americana(americana,loteria, sorteo)

            elif(loteria == 'New York' and sorteo == 'PM'):
                self.lote = NEW_TORK_NOCHE_TODO
                self.premiar_americana(americana,loteria, sorteo)

            elif(loteria == 'Florida' and sorteo == 'AM'):
                self.lote = FLORIDA_TARDE_TODO
                self.premiar_americana(americana,loteria,sorteo)

            elif(loteria == 'Florida' and sorteo == 'PM'):
                self.lote = FLORIDA_NOCHE_TODO
                self.premiar_americana(americana,loteria,sorteo)

    def premiar_americana(self, americana, loteria, sorteo):
        URL_1 = Obtener(americana, self.lote[0]).devolver_numeros()
        self.prueeee = URL_1
        URL_2 = Obtener(americana, self.lote[1]).devolver_numeros()
        #URL_3 = Obtener(True,self.lote[2]).devolver_numeros()

        if(URL_1 == URL_2 and URL_1!='' and URL_2!='' ):
            print("LOS NUMEROS SON IGUALES")
            Premio(url, 'carlos@premio',1234,loteria,URL_1, sorteo )
            borrarPantalla()
            print(f'NUMEROS PUBLICADOS...')
            return URL_1
        else:
            print('Los Numeros Son Diferentes O No existen')

#main(True,'New York','AM')
#main(True,'New York','PM')
#main(True,'Florida', 'AM')
#main(True, 'Florida', 'PM')
#print(main(True,'New York','AM').prueeee)