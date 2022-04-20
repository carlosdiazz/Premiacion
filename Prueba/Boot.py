from selenium import webdriver
from time import sleep
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import random

def sendKeysWithEmojis(element, text, driver):
    driver.execute_script(
        "arguments[0].value = '{}'; console.log(arguments[0].value)".format(text), element)
    element.send_keys('.')
    element.send_keys(Keys.BACKSPACE)
    element.send_keys(Keys.ENTER)

class Instabot:

    def __init__(self, username, password, postUrl, iniciar_en):

        driver = webdriver.Chrome(ChromeDriverManager().install())
        driver.get("https://www.instagram.com/")
        sleep(2)
        driver.find_element_by_xpath(
            "//input[@name=\"username\"]").send_keys(username)
        driver.find_element_by_xpath(
            "//input[@name=\"password\"]").send_keys(password)
        driver.find_element_by_xpath("//button[@type=\"submit\"]").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        driver.implicitly_wait(30)
        driver.find_element_by_xpath("//button[text()='Ahora no']").click()
        driver.implicitly_wait(30)
        driver.get(postUrl)

        lista = [
            '@carlosdiazz08',
            '@samuel_langumas',
            "@cepeda.enm",
            "@sppam.priv",
            "@juanluisdeolio",
            "@mariannysolis"
        ]
        candidad = 0

        while candidad < 100:
            for i in range(iniciar_en, len(lista)):
                print("pasando ", i)
                index = i
                driver.implicitly_wait(30)
                driver.find_element_by_xpath("//form").click()
                driver.implicitly_wait(30)
                element = driver.find_element_by_xpath("//textarea")
                if element:
                    palabra = random.choice(lista)
                    print("publicando ", palabra)
                    sendKeysWithEmojis(element, palabra, driver)
                sleep(15)
            candidad += 1

        print("candidad ", candidad * len(lista))
        print('index: ', index)
        if index == len(lista):
            print('***************************************************************')
            print('***************************************************************')
            print('EJECUCION TERMINADA CON EXITO')
            print('***************************************************************')
            print('***************************************************************')
        sleep(80)

Instabot('<USER>', '<PASSWORD>',
         'https://www.instagram.com/p/Cam6zNqrQEB/', 0)
