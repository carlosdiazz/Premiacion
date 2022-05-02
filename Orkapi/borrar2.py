from Funciones_Necesarias import fecha

fecha_dia_un_digito = fecha('%d')
fecha_dia_un_digito=fecha_dia_un_digito.lstrip('0')
Todas_las_Fechas = [

    fecha('%A, %b %d, %Y'),
    fecha(f'%A, %b {fecha_dia_un_digito}, %Y'),
    fecha('%A %B %dth %Y'),
    fecha('%a %m/%d/%y'),
    fecha('%A, %B %d, %Y'),
    fecha('%d-%m-%Y'),
    fecha('%d/%m/%Y'),
    fecha('%Y-%m-%d'),
    fecha(f'Sorteo: %d de {mes_espanol} del %Y.'),
    fecha('Resultados %d/%m/%Y'),
    ANGUILA_MANANA,
    ANGUILA_MEDIO_DIA,
    ANGUILA_TARDE,
    ANGUILA_NOCHE
    ]

print(Todas_las_Fechas)