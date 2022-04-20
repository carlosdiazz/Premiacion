from API_Numeros_Americanos import Obtener_Numeros_USA


from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_LOTTERY_USA_TARDE, FLORIDA_TARDE_TODO
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO

from Doble_Check import comprobar_iguales


#? Para consultar los numeros americanos se coloca asi.
#florida_page1 = Obtener_Numeros_USA(FLORIDA_LOTTERY_USA_TARDE).devolver_numeros()

#? Para comprobar que los numeros sean correctos de dos paginas distintas

florida_numeros = comprobar_iguales(FLORIDA_NOCHE_TODO)
print(florida_numeros)
