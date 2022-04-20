from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from Validar_Fecha import comprobar_sistema
import time

class Premio():

    def iniciar_Mac_Windows(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")
        self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)

    def iniciar_seccion(self, url, username, password):
        driver = self.driver
        driver.get(url)
        #Inicio seccion
        inputUsername = driver.find_element_by_xpath('//*[@id="usuario_username"]')
        inputUsername.send_keys(username)
        inputPassword = driver.find_element_by_xpath('//*[@id="usuario_password"]')
        inputPassword.send_keys(password)
        inputPassword.send_keys(Keys.ENTER)

    def colocar_Premio(self, loteria, premios, sorteo):
        #Busco el Premio
        driver = self.driver
        driver.get('https://dev_admin.orkapi.net/operaciones/premios/')
        time.sleep(2)

        inputLoteria = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[1]/div/input')
        inputLoteria.send_keys(loteria)
        time.sleep(2)

        inputLoteriaHora = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[4]/div/input')
        inputLoteriaHora.send_keys(sorteo)
        time.sleep(2)

        seleccionar = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]')
        seleccionar.click()
        time.sleep(2)

        #Colocar premio
        Primer_Premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input')
        Primer_Premio.send_keys(premios[0])
        time.sleep(2)
        Segundo_premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/input')
        Segundo_premio.send_keys(premios[1])
        time.sleep(2)
        Tercer_Premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/input')
        Tercer_Premio.send_keys(premios[2])
        time.sleep(2)
        boton_premiar = driver.find_element_by_xpath('//*[@id="index"]/div[2]/div/button[2]')
        boton_premiar.click()
        time.sleep(2)

    def __init__(self, url, username, password, loteria, premios, sorteo):

        if(comprobar_sistema() == 'Darwin'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()

        driver = self.driver
        self.iniciar_seccion(url=url ,username=username, password=password)
        self.colocar_Premio(loteria=loteria, premios=premios, sorteo=sorteo)
        driver.close()
