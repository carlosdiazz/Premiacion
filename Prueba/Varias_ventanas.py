from lib2to3.pgen2 import driver
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time



class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_cambiar_ventana(self):
        driver = self.driver
        driver.get('https://www.google.com.do/')
        time.sleep(3)

        driver.execute_script("window.open('');");
        time.sleep(2)

        driver.switch_to.window(driver.window_handles[1])
        driver.get('https://dev_admin.orkapi.net/operaciones/premios/')
        time.sleep(3)

        driver.switch_to.window(driver.window_handles[0])
        time.sleep(2)

if __name__ == '__main__':

    unittest.main()