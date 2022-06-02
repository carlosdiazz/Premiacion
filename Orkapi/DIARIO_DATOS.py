import schedule
from Funciones_Necesarias import fecha, borrarPantalla
import time
from Funciones_para_buscar_premios import Anguila_AM,La_Primera_AM,La_Suerte,King_Lottery_MD,Real,Anguila_MD,Florida_AM,Lotedom,New_York_AM
from Funciones_para_buscar_premios import Ganamas,Anguila_TARDE,King_Lottery_PM,Loteka,La_Primera_PM,Leidsa,Loteria_Nacional,Anguila_PM,Florida_PM,New_York_PM

#! ---------------------------------------------------------
schedule.every().day.at("10:05:00").do(Anguila_AM)
schedule.every().day.at("12:05:00").do(La_Primera_AM)
schedule.every().day.at("12:35:00").do(La_Suerte)
schedule.every().day.at("12:35:00").do(King_Lottery_MD)
schedule.every().day.at("13:10:00").do(Real)
schedule.every().day.at("13:05:00").do(Anguila_MD)
schedule.every().day.at("13:45:00").do(Florida_AM)
schedule.every().day.at("14:05:00").do(Lotedom)
schedule.every().day.at("14:30:00").do(New_York_AM)
schedule.every().day.at("14:35:00").do(Ganamas)
schedule.every().day.at("18:05:00").do(Anguila_TARDE)
schedule.every().day.at("19:35:00").do(King_Lottery_PM)
schedule.every().day.at("20:05:00").do(Loteka)
schedule.every().day.at("20:05:00").do(La_Primera_PM)
schedule.every().day.at("21:11:00").do(Leidsa)
schedule.every().day.at("21:05:00").do(Loteria_Nacional)
schedule.every().day.at("21:10:00").do(Anguila_PM)
schedule.every().day.at("21:40:00").do(Florida_PM)
schedule.every().day.at("22:35:00").do(New_York_PM)


borrarPantalla()
while True:
    fecha_actual = fecha('%d-%m-%Y || %H:%M:%S')
    print(f"|----------> {fecha_actual} <----------|")
    saber = schedule.run_pending()
    if(saber == None):
        pass
    else:
        print(schedule.run_pending())
    time.sleep(60)