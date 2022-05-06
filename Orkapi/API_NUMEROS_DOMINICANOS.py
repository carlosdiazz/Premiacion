from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from Funciones_Necesarias import Validar_Fecha_Hoy, comprobar_sistema, solo_undigito
import time
try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("")

class Obtener_Numeros_DOMINICANOS():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #self.chrome_options.add_argument("--headless")
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
            time.sleep(5)
            driver.get(datos['URL'][1])
            time.sleep(10)
        try:
            element = WebDriverWait(driver,10).until(
                EC.presence_of_element_located((By.XPATH, datos['FECHA'][0]))
            )
        except:
            self.fecha = False
        finally:
            self.fecha = element.text

        if(Validar_Fecha_Hoy(self.fecha)):
            self.fecha_elemento = self.fecha
            element.location_once_scrolled_into_view
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
        numero=[]
        for i in range(3):
            try:
                numero_actual=WebDriverWait(driver,10).until(
                    EC.presence_of_element_located((By.XPATH, datos['NUMEROS'][i]))
                )
            except:
                break
            finally:
                if(numero_actual.text != ""):
                    driver.save_screenshot('LOTERIA_PAGES.png')
                    numero.append(numero_actual.text)

        time.sleep(2)
        if(len(numero)==3):
            #! FUNCION CON NUMERO 00 ANGUILA
            #if(numero[0] == 0 and numero[1] == 0)
            
            return [
                self.fecha_elemento,
                solo_undigito(numero[0]),
                solo_undigito(numero[1]),
                solo_undigito(numero[2])
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