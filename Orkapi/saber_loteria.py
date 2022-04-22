def saberloteriaBOT(message):

    if(message == '/Premiar_Real'  ):
        return ['REAL', 'LOTERIA QUIN-PALE-TRIP 1:00 PM']

    elif(message == '/Premiar_New_York_PM' or message == '/Obtener_New_York_PM'):
        return ['New York', 'NEW YORK PM Inicio: 06:00:00 AM Cierre: 10:20:00 PM']

    elif(message == '/Premiar_New_York_AM' or message == '/Obtener_New_York_AM'):
        return ['New York', 'NEW YORK AM Inicio: 06:00:00 AM Cierre: 02:20:00 PM']

    elif(message == '/Premiar_Florida_PM' or message == '/Obtener_Florida_PM'):
        return ['Florida', 'FLORIDA PM Inicio: 06:00:00 AM Cierre: 09:40:00 PM']

    elif(message == '/Premiar_Florida_AM' or message == '/Obtener_Florida_AM'):
        return ['Florida', 'FLORIDA AM Inicio: 06:00:00 AM Cierre: 01:25:00 PM']
