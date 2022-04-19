import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())

    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get('https://www.google.com.do')
        time.sleep(3)
        driver.get('https://www.google.com.do/search?q=sad&source=hp&ei=LuNdYtytMMCbwbkP_NiP6As&iflsig=AHkkrS4AAAAAYl3xPtE1GvpRygNEECTlMbU_Dx3rcuTE&ved=0ahUKEwjc_KLe0Z73AhXATTABHXzsA70Q4dUDCAc&uact=5&oq=sad&gs_lcp=Cgdnd3Mtd2l6EAMyCwguEIAEELEDENQCMgUIABCABDIICAAQgAQQsQMyBQguEIAEMgUILhCABDIFCC4QgAQyCAguEIAEENQCMgUIABCABDIFCAAQgAQyBQguEIAEOg4IABCPARDqAhCMAxDlAjoOCC4QjwEQ6gIQjAMQ5QI6DgguEIAEELEDEMcBEKMCOg4ILhCABBCxAxDHARDRAzoECAAQA1BvWHlgkANoAXAAeAGAAXqIAboCkgEDMi4xmAEAoAEBsAEK&sclient=gws-wiz')
        time.sleep(5)
        buscar_xpath = driver.find_element_by_xpath('/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
        buscar_xpath.send_keys('sdsdds')
        buscar_xpath.send_keys(Keys.RETURN)
        time.sleep(5)

    def tearDown(self):
        self.driver.close()

if __name__ == '__main__':

    unittest.main()