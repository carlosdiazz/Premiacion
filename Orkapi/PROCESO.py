from Doble_Check import comprobar_iguales
from DATOS_LOTERIAS.Datos_FL_NOCHES import FLORIDA_NOCHE_TODO
from DATOS_LOTERIAS.Datos_FL_TARDE import FLORIDA_TARDE_TODO
from DATOS_LOTERIAS.Datos_NY_NOCHE import NEW_TORK_NOCHE_TODO
from DATOS_LOTERIAS.Datos_NY_TARDE import NEW_YORK_TARDE_TODO


def PROCESO(loteria, horario):

    if(loteria == 'Florida' and horario == 'AM'):
        return comprobar_iguales(FLORIDA_TARDE_TODO)

    elif(loteria == 'Florida' and horario == 'PM'):
        return comprobar_iguales(FLORIDA_NOCHE_TODO)

    elif(loteria == 'New York' and horario == 'AM'):
        return comprobar_iguales(NEW_YORK_TARDE_TODO)

    elif(loteria == 'New York' and horario == 'PM'):
        return comprobar_iguales(NEW_TORK_NOCHE_TODO)

    else:
        return False