from selenium import webdriver
from Funciones_Necesarias import comprobar_sistema, Saber_Loteria_Seleccionada
from time import sleep
from DATOS_LOTERIAS.PLATAFORMA import PLATAFORMA_TODO

try:
    from webdriver_manager.chrome import ChromeDriverManager
except:
    print("")

class Colocar_Numeros_Plataforma():

    def iniciar_Mac_Windows(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        self.chrome_options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=self.chrome_options)
        except:
            print("\n\nEsto es Ubuntu\n\n")

    def iniciar_Ubuntu(self):
        self.driver_location = "/snap/bin/chromium.chromedriver"
        self.binary_location = '/usr/bin/chromium-browser'
        self.options = webdriver.ChromeOptions()
        self.options.binary_location = self.binary_location
        self.options.add_argument("--headless")
        try:
            self.driver = webdriver.Chrome(executable_path=self.driver_location, chrome_options=self.options)
        except:
            print("\n\nEsto es WIndows\n\n")

    def iniciar_seccion(self,URL,USER,PASSWORD):
        try:
            driver = self.driver
            driver.get(URL)
            sleep(1)
            inputUSERR = driver.find_element_by_xpath(PLATAFORMA_TODO[2]).send_keys(USER)
            sleep(1)
            inputPASS = driver.find_element_by_xpath(PLATAFORMA_TODO[3]).send_keys(PASSWORD)
            sleep(1)
            BotonLogin = driver.find_element_by_xpath(PLATAFORMA_TODO[4]).click()
            sleep(1)
            return True
        except:
            return 'No se pudo iniciar seccion'

    def Buscar_Loteria(self,LOTERIA,SORTEO):
        try:
            driver = self.driver
            driver.get(PLATAFORMA_TODO[1])
            sleep(2)
            inputLoteria = driver.find_element_by_xpath(PLATAFORMA_TODO[5]).send_keys(LOTERIA)
            sleep(3)
            inputSorteo = driver.find_element_by_xpath(PLATAFORMA_TODO[6]).send_keys(SORTEO)
            sleep(3)
            selecionarLo = driver.find_element_by_xpath(PLATAFORMA_TODO[7]).click()
            sleep(2)
            Loteria_seleccinanda = driver.find_element_by_xpath(PLATAFORMA_TODO[12]).text

            if(Saber_Loteria_Seleccionada(Loteria_seleccinanda, SORTEO)):
                return True
        except:
            self.resultado= f'No se encontro esta Loteria: {LOTERIA} o este Sorteo: {SORTEO}'

    def Premiar(self,LOTERIA,SORTEO,PREMIOS):
        try:
            driver = self.driver
            comprobarPremiado = driver.find_element_by_xpath(PLATAFORMA_TODO[8]).is_enabled()
            if(comprobarPremiado):
                Primer_Premio = driver.find_element_by_xpath(PLATAFORMA_TODO[8]).send_keys(PREMIOS[0])
                sleep(2)
                Segundo_Premio =  driver.find_element_by_xpath(PLATAFORMA_TODO[9]).send_keys(PREMIOS[1])
                sleep(2)
                Tercer_Premio = driver.find_element_by_xpath(PLATAFORMA_TODO[10]).send_keys(PREMIOS[2])
                sleep(2)
                boton_premiar = driver.find_element_by_xpath(PLATAFORMA_TODO[11])
                sleep(2)
                boton_premiar.click()
                sleep(4)
                self.resultado = True
                driver.save_screenshot('premiada.png')
            else:
                self.resultado = 'Esta Loteria esta Premiada'
        except:
            self.resultado= f'No se pudo Premiar esta Loteria: {LOTERIA} con este Sorteo: {SORTEO}'

    def Resultadoo(self):
        try:
            if(self.resultado == True):
                return True
            else:
                return self.resultado
        except:
            return self.resultado

    def __init__(self,URL,USER,PASSWORD,LOTERIA,SORTEO,PREMIOS ) :
        self.resultado = 'No se logro completar la Premiacion'
        if(comprobar_sistema() == 'Darwin' or comprobar_sistema() == 'Windows'):
            self.iniciar_Mac_Windows()
        else:
            self.iniciar_Ubuntu()
        Iniciar = self.iniciar_seccion(URL,USER,PASSWORD)

        if(Iniciar == True):
            Loteria=self.Buscar_Loteria(LOTERIA,SORTEO)
            if(Loteria == True):
                self.Premiar(LOTERIA,SORTEO,PREMIOS)

        else:
            self.resultado = 'No se pudo iniciar Seccion'