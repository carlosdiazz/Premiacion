from API_Numeros_Americanos import Obtener_Numeros_USA
from API_NUMEROS_DOMINICANOS import Obtener_Numeros_DOMINICANOS
def Doble_Check(Lista_de_pagina):

    if(Lista_de_pagina):
        if(Lista_de_pagina[2]):
            URL1= Obtener_Numeros_USA(Lista_de_pagina[0]).devolver_numeros()
            URL2= Obtener_Numeros_USA(Lista_de_pagina[1]).devolver_numeros()

            if(URL1 and URL2):
                if(URL1[1:] == URL2[1:] ):
                    return URL1[1:]
                else:
                    return False
            else:
                return False
        else:
            URL1= Obtener_Numeros_DOMINICANOS(Lista_de_pagina[0]).devolver_numeros()
            if(URL1):
                return URL1[1:]
    else:
        return False