def saberloteriaBOT(message):

    if(message == '/Premiar_Real'  ):
        return ['REAL', 'LOTERIA QUIN-PALE-TRIP 1:00 PM']

    elif(message == '/Premiar_New_York_PM' or message == '/Obtener_New_York_PM'):
        return ['New York', 'PM']

    elif(message == '/Premiar_New_York_AM' or message == '/Obtener_New_York_AM'):
        return ['New York', 'AM']

    elif(message == '/Premiar_Florida_PM' or message == '/Obtener_Florida_PM'):
        return ['Florida', 'PM']

    elif(message == '/Premiar_Florida_AM' or message == '/Obtener_Florida_AM'):
        return ['Florida', 'AM']
