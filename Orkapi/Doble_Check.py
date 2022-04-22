from API_Numeros_Americanos import Obtener_Numeros_USA

def comprobar_iguales(Lista_de_pagina):
    URL1= Obtener_Numeros_USA(Lista_de_pagina[0]).devolver_numeros()
    URL2= Obtener_Numeros_USA(Lista_de_pagina[1]).devolver_numeros()

    if(URL1 == URL2 and URL1 !="" and URL2 !=""):
        return URL1
    else:
        return False