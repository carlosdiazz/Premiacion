from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Funciones_Necesarias import Validar_Fecha_Hoy, borrarPantalla, comprobar_sistema, solo_undigito
import time
from DATOS_LOTERIAS.Datos_La_suerte import La_suerte_Todo
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("ChromeDriverManager no Existe")

from DATOS_LOTERIAS.Datos_Loteka import Loteka_Todo

class Obtener_Numeros_DOMINICANOS():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        except:
            print("Esto es Ubuntu")

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)

    def obtener_Fecha(self):
        driver = self.driver
        datos = self.datos
        if(len(datos['URL']) == 3):
            driver.get(datos['URL'][0])
            time.sleep(5)
            cerrar = driver.find_element_by_xpath(datos['URL'][2])
            time.sleep(5)
            cerrar.click()
        else:
            driver.get(datos['URL'][0])
            driver.get(datos['URL'][1])
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, datos['FECHA'][0]))
            )
        finally:
            self.fecha = element.text

        if(Validar_Fecha_Hoy(self.fecha)):
            self.fecha_elemento = self.fecha
            return True
        else:
            return False

    def obtener_numeros(self):
        driver = self.driver
        datos = self.datos

        if(len(datos['URL']) == 3):
                time.sleep(1)
        else:
            driver.get(datos['URL'][0])
            driver.get(datos['URL'][1])
        time.sleep(2)
        numero_1 = driver.find_element_by_xpath(datos['NUMEROS'][0]).text
        numero_2 = driver.find_element_by_xpath(datos['NUMEROS'][1]).text
        numero_3 = driver.find_element_by_xpath(datos['NUMEROS'][2]).text
        time.sleep(2)

        if(numero_1 and numero_2 and numero_3):
            return [
                self.fecha_elemento,
                solo_undigito(numero_1),
                solo_undigito(numero_2),
                solo_undigito(numero_3)
            ]
        else:
            return False

    def devolver_numeros(self):
        try:
            if(self.obtener_Fecha()):
                return self.obtener_numeros()
            else:
                return False
        except:
            return False

    def __init__(self, datos) :
        if(comprobar_sistema() == 'Darwin' or comprobar_sistema() == 'Windows'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()
        self.datos=datos