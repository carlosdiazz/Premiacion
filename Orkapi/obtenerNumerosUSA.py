from lib2to3.pgen2 import driver
from traceback import print_tb
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import os
from datetime import datetime
import time

class Numeros():

    def setUp(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])
        #chrome_options.add_argument("--headless")
        self.driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)

    def obtener_numbers(self, numbers, xpath_fecha, xpath_num1, xpath_num2):
        driver = self.driver
        Link_Numbers = numbers
        driver.get(Link_Numbers)

        fechaHoy = datetime.today().strftime('%A, %B %d, %Y')
        fechaHoy2 = datetime.today().strftime('%A, %b %d, %Y')
        #fechaHoy = 'Sunday, April 17, 2022'
        fecha_numbers = driver.find_element_by_xpath(xpath_fecha).text

        if(fechaHoy == fecha_numbers or fechaHoy2 == fecha_numbers):
            print("la fecha es de HOY")
            num1 = driver.find_element_by_xpath(xpath_num1).text
            num2 = driver.find_element_by_xpath(xpath_num2).text
            self.primer_numero = num1 + num2
            time.sleep(2)
        else:
            print("No es la fecha correcta")
            self.primer_numero = ''
            time.sleep(5)

    def obtener_win4(self,win4, xpath_fecha, xpath_number3, xpath_number4, xpath_number5, xpath_number6):\

        driver = self.driver
        Link_win4 = win4
        driver.get(Link_win4)

        fechaHoy = datetime.today().strftime('%A, %B %d, %Y')
        fechaHoy2 = datetime.today().strftime('%A, %b %d, %Y')
        #fechaHoy = 'Sunday, April 17, 2022'
        fecha_win = driver.find_element_by_xpath(xpath_fecha).text

        if(fecha_win == fechaHoy or fechaHoy2 == fecha_win ):
            print("la fecha es de HOY")
            num3 = driver.find_element_by_xpath(xpath_number3).text
            num4 = driver.find_element_by_xpath(xpath_number4).text
            self.segundo_numero = num3 + num4

            num5 = driver.find_element_by_xpath(xpath_number5).text
            num6 = driver.find_element_by_xpath(xpath_number6).text
            self.tercer_numero = num5 + num6
            time.sleep(2)
        else:
            print("No es la fecha correcta")
            self.segundo_numero = ''
            self.tercer_numero = ''

    def obtener_Todo(self):
        if(self.primer_numero and self.segundo_numero and self.tercer_numero ):
            print("Obteniendo Numeros")
            print(f'{self.primer_numero} - {self.segundo_numero} - {self.tercer_numero}')
            time.sleep(5)
            return [self.primer_numero, self.segundo_numero, self.tercer_numero]
        else:
            return False

    def __init__(self, arr):

        numbers         = arr[0]
        wind4           = arr[4]
        xpath_fecha_1   = arr[1]
        xpath_num1      = arr[2]
        xpath_num2      = arr[3]
        xpath_fecha_2   = arr[5]
        xpath_num3      = arr[6]
        xpath_num4      = arr[7]
        xpath_num5      = arr[8]
        xpath_num6      = arr[9]
        os.system('cls')
        self.setUp()
        os.system('cls')
        self.obtener_numbers(numbers, xpath_fecha_1, xpath_num1, xpath_num2 )
        os.system('cls')
        self.obtener_win4(wind4,xpath_fecha_2,xpath_num3, xpath_num4, xpath_num5, xpath_num6 )
        os.system('cls')
        self.driver.close()
