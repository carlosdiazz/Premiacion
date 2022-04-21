from datetime import datetime

def fecha(tipo_fecha):
    return datetime.today().strftime(tipo_fecha)




def Validar_Fecha_Hoy(fecha_comprobar):

    Todas_las_Fechas = [
        fecha('%A, %b %d, %Y'),
        fecha('%A %B %dth %Y'),
        fecha('%a %m/%d/%y'),
        fecha('%A, %B %d, %Y')
        ]
    if fecha_comprobar in Todas_las_Fechas:
        return True
    else:
        return False

print(fecha('%A, %b %d, %Y'))
print(fecha('%d-%m-%Y'))