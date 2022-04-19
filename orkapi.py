import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class Premio():

    def __init__(self, url, username, password, loteria, premios):

        #Abro la pagina
        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get(url)

        #Inicio seccion
        inputUsername = driver.find_element_by_xpath('//*[@id="usuario_username"]')
        inputUsername.send_keys(username)
        inputPassword = driver.find_element_by_xpath('//*[@id="usuario_password"]')
        inputPassword.send_keys(password)
        inputPassword.send_keys(Keys.ENTER)

        #Busco el Premio
        driver.get('https://dev_admin.orkapi.net/operaciones/premios/')

        inputLoteria = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/thead/tr[2]/th[1]/div/input')
        inputLoteria.send_keys(loteria)

        seleccionar = driver.find_element_by_xpath('/html/body/div[2]/div/div/div/div[2]/div[1]/div[2]/div/table/tbody/tr/td[1]')
        seleccionar.click()

        #Colocar premio
        Primer_Premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[1]/td[2]/div/input')
        Primer_Premio.send_keys(premios[0])
        time.sleep(1)

        Segundo_premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[2]/td[2]/div/input')
        Segundo_premio.send_keys(premios[1])
        time.sleep(1)

        Tercer_Premio = driver.find_element_by_xpath('//*[@id="index"]/div[1]/div/div/div/div/div[2]/div/table/tbody/tr[3]/td[2]/div/input')
        Tercer_Premio.send_keys(premios[2])
        time.sleep(1)

        boton_premiar = driver.find_element_by_xpath('//*[@id="index"]/div[2]/div/button[2]')
        boton_premiar.click()
        time.sleep(5)
        driver.close()