import schedule
import time
import threading
from Class_Premiar_Automatico import Premiar_Loterias_
from Funciones_Necesarias import fecha
from TOKEN_API_PRO_DE import plataforma_Desarrollo, plataforma_Mega_Lottery

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()


#! Aqui esta todo lo necesario apra poder premiar de forma automatica diferentes plataforma

#! PLATFORMA DE DESARROLLO ---------------------------------------------------------------------------------
DEV_Anguila_AM_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_AM',plataforma_Desarrollo).Premiar_Loterias
DEV_PRIMERA_AM_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Primera_AM',plataforma_Desarrollo).Premiar_Loterias
DEV_LA_SUERTE_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Suerte',plataforma_Desarrollo).Premiar_Loterias
DEV_ANGUILA_MD_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_MD',plataforma_Desarrollo).Premiar_Loterias
DEV_REAL_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Real',plataforma_Desarrollo).Premiar_Loterias
DEV_FLORIDA_AM_PREMIOS = Premiar_Loterias_('/Premiar_Florida_AM',plataforma_Desarrollo).Premiar_Loterias
DEV_LOTEDOM_PREMIOS = Premiar_Loterias_('/Premiar_Lotedom',plataforma_Desarrollo).Premiar_Loterias
DEV_NEW_YORK_AM_PREMIOS = Premiar_Loterias_('/Premiar_New_York_AM',plataforma_Desarrollo).Premiar_Loterias
DEV_Ganams_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Ganamas',plataforma_Desarrollo).Premiar_Loterias
DEV_ANGUILA_TARDE_PREMIOS = Premiar_Loterias_('/Premiar_Anguila_TARDE',plataforma_Desarrollo).Premiar_Loterias
DEV_LOTEKA_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Loteka',plataforma_Desarrollo).Premiar_Loterias
DEV_PRIMERA_PM_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Primera_PM',plataforma_Desarrollo).Premiar_Loterias
DEV_LOTERIA_NACIONAL_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Nacional',plataforma_Desarrollo).Premiar_Loterias
DEV_LEIDSA_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_Leidsa',plataforma_Desarrollo).Premiar_Loterias
DEV_ANGUILA_NOCHE = Premiar_Loterias_('/Premiar_Anguila_NOCHE',plataforma_Desarrollo).Premiar_Loterias
DEV_FLORIDA_PM_PREMIOS = Premiar_Loterias_('/Premiar_Florida_PM',plataforma_Desarrollo).Premiar_Loterias
DEV_New_York_PM_Premios = Premiar_Loterias_('/Premiar_New_York_PM',plataforma_Desarrollo).Premiar_Loterias

#! PLATAFORMA MEGALOTERRY -----------------------------------------------------------------------------------------
MGL_PRIMERA_PM_PREMIOS = Premiar_Loterias_('/Premiar_Loteria_La_Primera_PM',plataforma_Mega_Lottery).Premiar_Loterias




#? HORARIOS PLATAFORMA DESARROLLO=====================================================================
schedule.every().day.at("10:05:00").do(run_threaded, DEV_Anguila_AM_PREMIOS)
schedule.every().day.at("12:05:00").do(run_threaded, DEV_PRIMERA_AM_PREMIOS)
schedule.every().day.at("12:35:00").do(run_threaded, DEV_LA_SUERTE_PREMIOS)
schedule.every().day.at("13:05:00").do(run_threaded, DEV_ANGUILA_MD_PREMIOS)
schedule.every().day.at("13:05:00").do(run_threaded, DEV_REAL_PREMIOS)
schedule.every().day.at("13:50:00").do(run_threaded, DEV_FLORIDA_AM_PREMIOS)
schedule.every().day.at("14:05:00").do(run_threaded, DEV_LOTEDOM_PREMIOS)
schedule.every().day.at("14:35:00").do(run_threaded, DEV_NEW_YORK_AM_PREMIOS)
schedule.every().day.at("14:40:00").do(run_threaded, DEV_Ganams_PREMIOS)
schedule.every().day.at("18:05:00").do(run_threaded, DEV_ANGUILA_TARDE_PREMIOS)
schedule.every().day.at("20:05:00").do(run_threaded, DEV_LOTEKA_PREMIOS)
schedule.every().day.at("20:05:00").do(run_threaded, DEV_PRIMERA_PM_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, DEV_LOTERIA_NACIONAL_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, DEV_LEIDSA_PREMIOS)
schedule.every().day.at("21:05:00").do(run_threaded, DEV_ANGUILA_NOCHE)
schedule.every().day.at("21:50:00").do(run_threaded, DEV_FLORIDA_PM_PREMIOS)
schedule.every().day.at("22:35:00").do(run_threaded, DEV_New_York_PM_Premios)
#!--------------------------------DOMINGO-------------------------------
schedule.every().sunday.at("15:55:00").do(run_threaded, DEV_LEIDSA_PREMIOS)
schedule.every().sunday.at("18:05:00").do(run_threaded, DEV_LOTERIA_NACIONAL_PREMIOS)

#? PLATAFORMA MEGA LOTTERY ------------------------------------------------
schedule.every().day.at("20:05:00").do(run_threaded, MGL_PRIMERA_PM_PREMIOS)

#borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|-- PREMIOS --> {fecha_actual} <-- PREMIOS --|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(60)