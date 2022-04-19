import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time


driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get("https://dev_admin.orkapi.net/login/")

#Aqui busco un elemneto y le mando ddatos
usuario = driver.find_element_by_id("usuario_username")
usuario.send_keys('carlos@orkapi')

passw = driver.find_element_by_id("usuario_password")
passw.send_keys('1234')
passw.send_keys(Keys.ENTER)


time.sleep(5)
driver.close()