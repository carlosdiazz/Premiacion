from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Funciones_Necesarias import Validar_Fecha_Hoy, comprobar_sistema
import time

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("ChromeDriverManager no Existe")
class Obtener_Numeros_USA():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
            self.driver.maximize_window()
        except:
            print("Esto es Ubuntu")

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        #self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)
        self.driver.maximize_window()

    def americana_tres(self, datos):
        driver = self.driver
        try:
            driver.get(datos['URL'][0])
            driver.get(datos['URL'][1])
            time.sleep(1)
            self.fecha_tres = driver.find_element_by_xpath(datos['TRES'][0]).text
            self.tres=''

            if(Validar_Fecha_Hoy(self.fecha_tres)):
                for i in range (1,3):
                    try:
                        element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH,datos['TRES'][i]) )
                        )

                    finally:
                        self.tres+=element.text
            else:
                self.tres=False
        except :
            self.tres=False

    def americana_cuatro(self, datos):
        driver = self.driver
        try:
            driver.get(datos['URL'][0])
            driver.get(datos['URL'][2])
            time.sleep(1)
            self.fecha_cuatro = driver.find_element_by_xpath(datos['CUATRO'][0]).text
            self.cuatro=''

            if(Validar_Fecha_Hoy(self.fecha_cuatro)):
                for i in range (1,5):
                    try:
                        element = WebDriverWait(driver, 10).until(
                        EC.visibility_of_element_located((By.XPATH,datos['CUATRO'][i]) )
                        )
                    finally:
                        self.cuatro+=element.text
            else:
                self.cuatro=False
        except:
            self.cuatro=False

    def devolver_numeros(self):
        if(self.tres and self.cuatro):
            #! ----------------------------------------------------------------------------------------------- self.fecha_cuatro == self.fecha_tres
            if(self.fecha_cuatro == self.fecha_tres):
                self.driver.save_screenshot('LOTERIA_PAGES.png')
                return [self.fecha_cuatro,self.tres, self.cuatro[0:2], self.cuatro[2:4]]
            else:
                return False
        else:
            return False

    def __init__(self, datos) :
        if(comprobar_sistema() == 'Darwin' or comprobar_sistema() == 'Windows'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()

        self.americana_tres(datos)
        self.americana_cuatro(datos)