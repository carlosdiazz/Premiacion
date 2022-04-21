from Doble_Check import comprobar_iguales
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_TARDE_TODO
from DATOS_LOTERIAS.Datos_NY_NOCHE import NEW_TORK_NOCHE_TODO
from DATOS_LOTERIAS.Datos_NY_TARDE import NEW_YORK_TARDE_TODO
from DATOS_LOTERIAS.Datos_Real import LOTO_REAL_TODO
from API_NUMEROS_DOMINICANOS import Obtener_Numeros_DOMINICANOS
from DATOS_LOTERIAS.Datos_Real import Loto_Real_Oficial_todo


def PROCESO(loteria, horario):

    if(loteria == 'Florida' and horario == 'AM'):
        return comprobar_iguales(FLORIDA_TARDE_TODO)

    elif(loteria == 'Florida' and horario == 'PM'):
        return comprobar_iguales(FLORIDA_NOCHE_TODO)

    elif(loteria == 'New York' and horario == 'AM'):
        return comprobar_iguales(NEW_YORK_TARDE_TODO)

    elif(loteria == 'New York' and horario == 'PM'):
        return comprobar_iguales(NEW_TORK_NOCHE_TODO)

    elif(loteria == 'REAL' and horario == 'REAL'):
        return Obtener_Numeros_DOMINICANOS(Loto_Real_Oficial_todo).devolver_numeros()

    else:
        return False