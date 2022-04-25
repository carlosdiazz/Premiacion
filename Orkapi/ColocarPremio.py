from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from Funciones_Necesarias import  borrarPantalla, comprobar_sistema
import time

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("ChromeDriverManager no Existe")
class Colocar_Numeros_Plataforma():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        except:
            print("Esto es Ubuntu")
        #borrarPantalla()

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)
        #borrarPantalla()

    def iniciar_seccion(self, URL, USERNAME, PASSWORD):
        driver = self.driver
        driver.get(URL)
        time.sleep(2)
        #Inicio seccion
        inputUsername = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/form/div[2]/div/input')
        inputUsername.send_keys(USERNAME)
        inputPassword = driver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/form/div[3]/div/input')
        inputPassword.send_keys(PASSWORD)
        inputPassword.send_keys(Keys.ENTER)
        time.sleep(1)

    def colocar_premios(self, LOTERIA, HORARIO, PREMIO):
        #Busco el Premio
        driver = self.driver
        driver.get('https://dev_admin.orkapi.net/operaciones/premios/')
        time.sleep(2)

        inputLoteria = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[1]/div/input')
        inputLoteria.send_keys(LOTERIA)
        time.sleep(3)

        inputLoteriaHora = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[4]/div/input')
        inputLoteriaHora.send_keys(HORARIO)
        time.sleep(3)
        seleccionar = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]')
        seleccionar.click()
        time.sleep(2)

        comprobarPremiado = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input').is_enabled()
        if(comprobarPremiado):
            Primer_Premio = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input')
            Primer_Premio.send_keys(PREMIO[0])
            time.sleep(1)
            Segundo_premio = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/input')
            Segundo_premio.send_keys(PREMIO[1])
            time.sleep(1)
            Tercer_Premio = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/input')
            Tercer_Premio.send_keys(PREMIO[2])
            time.sleep(1)
            boton_premiar = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[2]/div[3]/form/div[2]/div/button[2]')
            time.sleep(1)
            boton_premiar.click()
            time.sleep(5)
            self.resultado = True
        else:
            self.resultado = False

    def resultado_final(self):
        try:
            if(self.resultado):
                return True
            else:
                return False
        except:
            return False
    def __init__(self, URL, USERNAME, PASSWORD, LOTERIA, HORARIO, PREMIOS ) :
        if(comprobar_sistema() == 'Darwin' or comprobar_sistema() == 'Windows'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()

        self.iniciar_seccion(URL,USERNAME, PASSWORD)
        self.colocar_premios(LOTERIA, HORARIO, PREMIOS)