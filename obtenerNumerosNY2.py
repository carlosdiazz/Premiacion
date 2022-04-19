from traceback import print_tb
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time
import os
from datetime import datetime


def Numeros_New_York2():

    numbers = 'https://www.lotterypost.com/game/146/results'
    win4 = 'https://www.lotterypost.com/game/149/results'
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(numbers)
    #time.sleep(5)

    fechaHoy = datetime.today().strftime('%A, %B %d, %Y')
    #fechaHoy = 'Sunday, April 17, 2022'
    fecha_numbers = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]').text
    #time.sleep(2)

    if(fecha_numbers == fechaHoy):
        #Numbers Evening
        num1 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]').text
        num2 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]').text
        primer_numero = num1 + num2
        #time.sleep(2)
        driver.get(win4)

        fecha_win = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[1]').text
        if(fecha_win == fechaHoy ):
        #Win 4 Evening
            num3 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[1]').text
            num4 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[2]').text
            segundo_numero = num3 + num4

            num5 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[3]').text
            num6 = driver.find_element_by_xpath('//*[@id="resultsTable"]/table/tbody/tr[1]/td/div/div[2]/div[2]/ul/li[4]').text
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
Numeros_New_York2()