from traceback import print_tb
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
from datetime import datetime


def Numeros_New_York():

    numbers = 'https://www.lotteryusa.com/new-york/numbers/'
    win4 = 'https://www.lotteryusa.com/new-york/win-4/'
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(ChromeDriverManager().install(), options=chrome_options)
    driver.get(numbers)
    #time.sleep(5)

    fechaHoy = datetime.today().strftime('%A, %b %d, %Y')
    #fechaHoy = 'Sunday, Apr 17, 2022'
    fecha_numbers = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time').text
    #time.sleep(2)

    if(fecha_numbers == fechaHoy):
        #Numbers Evening
        num1 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span').text
        num2 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span').text
        primer_numero = num1 + num2
        #time.sleep(2)
        driver.get(win4)

        fecha_win = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/th/time').text
        if(fecha_win == fechaHoy ):
        #Win 4 Evening
            num3 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[1]/span').text
            num4 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[2]/span').text
            segundo_numero = num3 + num4

            num5 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[3]/span').text
            num6 = driver.find_element_by_xpath('//*[@id="main"]/div[3]/div/div[2]/div[1]/table/tbody/tr[1]/td[1]/div/ul/li[4]/span').text
            tercer_numero = num5 + num6
            #time.sleep(2)

            driver.close()
            os.system('cls')
            #time.sleep(2)
            print(f'Los numeros son {primer_numero} - {segundo_numero} - {tercer_numero} ')
            return [primer_numero, segundo_numero, tercer_numero]
        else:
            print("Esta no es la fecha correcta")
            return False
    else:
        print("Esta no es la fecha correcta")
        return False
