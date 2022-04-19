import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time



class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_buscar(self):
        driver = self.driver
        driver.get('https://www.google.com.do')
        self.assertIn('Google' , driver.title)
        elemento = driver.find_element_by_name('q')
        elemento.send_keys('selenium')
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert 'Esta no es la pagina no es'

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':

    unittest.main()