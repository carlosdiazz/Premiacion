import schedule
from Funciones_Necesarias import fecha, borrarPantalla
import time
from Funciones_para_buscar_premios import Anguila_AM,La_Primera_AM,La_Suerte,King_Lottery_MD,Real,Anguila_MD,Florida_AM,Lotedom,New_York_AM
from Funciones_para_buscar_premios import Ganamas,Anguila_TARDE,King_Lottery_PM,Loteka,La_Primera_PM,Leidsa,Loteria_Nacional,Anguila_PM,Florida_PM,New_York_PM
import threading

def run_threaded(job_func):
    job_thread = threading.Thread(target=job_func)
    job_thread.start()

#! ---------------------------------------------------------
schedule.every().day.at("10:05:00").do(run_threaded, Anguila_AM)
schedule.every().day.at("12:05:00").do(run_threaded, La_Primera_AM)
schedule.every().day.at("12:35:00").do(run_threaded, La_Suerte)
schedule.every().day.at("12:35:00").do(run_threaded, King_Lottery_MD)
schedule.every().day.at("13:10:00").do(run_threaded, Real)
schedule.every().day.at("13:05:00").do(run_threaded, Anguila_MD)
schedule.every().day.at("13:45:00").do(run_threaded, Florida_AM)
schedule.every().day.at("14:05:00").do(run_threaded, Lotedom)
schedule.every().day.at("14:35:00").do(run_threaded, New_York_AM)
schedule.every().day.at("14:40:00").do(run_threaded, Ganamas)
schedule.every().day.at("18:05:00").do(run_threaded, Anguila_TARDE)
schedule.every().day.at("19:35:00").do(run_threaded, King_Lottery_PM)
schedule.every().day.at("20:05:00").do(run_threaded, Loteka)
schedule.every().day.at("20:05:00").do(run_threaded, La_Primera_PM)
schedule.every().day.at("21:11:00").do(run_threaded, Leidsa)
schedule.every().day.at("21:05:00").do(run_threaded, Loteria_Nacional)
schedule.every().day.at("21:10:00").do(run_threaded, Anguila_PM)
schedule.every().day.at("21:40:00").do(run_threaded, Florida_PM)
schedule.every().day.at("22:35:00").do(run_threaded, New_York_PM)

borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(30)