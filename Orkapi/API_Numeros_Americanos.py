
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Validar_Fecha import Validar_Fecha_Hoy, borrarPantalla, comprobar_sistema
import time

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("ChromeDriverManager no Existe")
class Obtener():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        except:
            print("sd")
        borrarPantalla()

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)


    def americana_tres(self, datos):
        driver = self.driver
        driver.get(datos['URL'][0])
        driver.get(datos['URL'][1])
        time.sleep(1)
        fecha_tres = driver.find_element_by_xpath(datos['TRES'][0]).text
        self.tres=''
        if(self.validar_fecha(fecha_tres)):
            for i in range (1,3):
                try:
                    element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,datos['TRES'][i]) )
                    )

                finally:
                    self.tres+=element.text
                    pass
        else:
            self.tres
        borrarPantalla()

    def americana_cuatro(self, datos):
        driver = self.driver
        driver.get(datos['URL'][0])
        driver.get(datos['URL'][2])
        self.cuatro=''
        fecha_cuatro = driver.find_element_by_xpath(datos['CUATRO'][0]).text
        if(self.validar_fecha(fecha_cuatro)):
            for i in range (1,5):
                try:
                    element = WebDriverWait(driver, 10).until(
                    EC.visibility_of_element_located((By.XPATH,datos['CUATRO'][i]) )
                    )

                finally:
                    self.cuatro+=element.text
                    pass
        else:
            self.cuatro
        borrarPantalla()

    def validar_fecha(self, fecha):
        return Validar_Fecha_Hoy(fecha)

    def devolver_numeros(self):
        if(self.tres and self.cuatro):
            return [self.tres, self.cuatro[0:2], self.cuatro[2:4]]
        else:
            return ""

    def __init__(self, americana, datos) :
        if(comprobar_sistema() == 'Darwin' or comprobar_sistema() == 'Windows'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()

        if(americana):
            self.americana_tres(datos)
            self.americana_cuatro(datos)
        else:
            pass