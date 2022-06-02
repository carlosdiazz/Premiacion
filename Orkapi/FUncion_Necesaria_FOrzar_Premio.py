from Funciones_para_buscar_premios import Anguila_AM, La_Primera_AM, La_Suerte, Real, Anguila_MD, Florida_AM, Lotedom, New_York_AM, Ganamas
from Funciones_para_buscar_premios import Anguila_TARDE, Loteka, La_Primera_PM, Loteria_Nacional, Leidsa, Anguila_PM, Florida_PM, New_York_PM
#! ---------------------------------------------------------------------

def Saber_Loteria_Forzada_Premio (loteria):

    if(loteria == '/Forzar_Premiar_Anguila_AM'):
        return Anguila_AM()

    elif(loteria == '/Forzar_Premiar_La_Primera_AM'):
        return La_Primera_AM()

    elif(loteria == '/Forzar_Premiar_Loteria_La_Suerte'):
        return La_Suerte()

    elif(loteria == '/Forzar_Premiar_Loteria_Real'):
        return Real()

    elif(loteria == '/Forzar_Premiar_Anguila_MD'):
        return Anguila_MD()

    elif(loteria == '/Forzar_Premiar_Florida_AM'):
        return Florida_AM()

    elif(loteria == '/Forzar_Premiar_Lotedom'):
        return Lotedom()

    elif(loteria == '/Forzar_Premiar_New_York_AM'):
        return New_York_AM()

    elif(loteria == '/Forzar_Premiar_Loteria_Ganamas'):
        return Ganamas()

    elif(loteria == '/Forzar_Premiar_Anguila_TARDE'):
        return Anguila_TARDE()

    elif(loteria == '/Forzar_Premiar_Loteria_Loteka'):
        return Loteka()

    elif(loteria == '/Forzar_Premiar_La_Primera_PM'):
        return La_Primera_PM()

    elif(loteria == '/Forzar_Premiar_Loteria_Nacional'):
        return Loteria_Nacional()

    elif(loteria == '/Forzar_Premiar_Loteria_Leidsa'):
        return Leidsa()

    elif(loteria == '/Forzar_Premiar_Anguila_NOCHE'):
        return Anguila_PM()

    elif(loteria == '/Forzar_Premiar_Florida_PM'):
        return Florida_PM()

    elif(loteria == '/Forzar_Premiar_New_York_PM'):
        return New_York_PM()

    else:
        print('Probando')