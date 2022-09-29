import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
import time


class TestNotifi(unittest.TestCase):

    def setUp(self):
        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serviceObj)
        # self.assertIn("Akcesoria, uchwyty, okucia meblowe - RustykalneUchwyty.pl", self.driver.title)

    def test_OrderSimpleProduct(self):
        self.counter = 0
        self.urls = ['https://dev321.seart.pl/rustykalne-masywne-lustro-country-25.html',
                     'https://dev321.seart.pl/rustykalna-konsola-drewniana-country-08.html',
                     'https://dev321.seart.pl/stelaz-samuraj-de-luxe-120.html']
        for url in self.urls:
            self.driver.get(url)
            self.driver.implicitly_wait(2)
            self.driver.maximize_window()
            self.driver.find_element(By.CSS_SELECTOR, "button[title='Do koszyka']").click()
            self.driver.find_element(By.CSS_SELECTOR, ".items").click()
            self.driver.find_element(By.CSS_SELECTOR, "div[class='totals'] button[title='Przejdź do kasy']").click()

            self.driver.find_element(By.XPATH, "//input[@id='billing:city']").send_keys("Miastoweeee")
            # uzupełnienie formularza zamowienia
            self.driver.find_element(By.XPATH, "//input[@id='billing:postcode']").send_keys("11-111")
            self.driver.find_element(By.CSS_SELECTOR, "label[for='agreement-1']").click()
            self.driver.find_element(By.CSS_SELECTOR, "label[for='agreement-3']").click()
            self.driver.find_element(By.XPATH, "//input[@id='billing:firstname']").send_keys("Wiktor")
            self.driver.find_element(By.XPATH, "//input[@id='billing:lastname']").send_keys("Testowy")
            self.driver.find_element(By.XPATH, "//input[@placeholder='nazwa@domena.pl']").send_keys(
                "jakisemail@seart.pl")
            self.driver.find_element(By.XPATH, "//input[@id='billing:telephone']").send_keys("555555555")
            self.driver.find_element(By.XPATH, "//input[@id='billing:street1']").send_keys("Adres adresowy 44")
            self.driver.find_element(By.XPATH, "//input[@id='billing:street2']").send_keys("4A")
            self.driver.find_element(By.XPATH, "//input[@id='billing:floor']").send_keys("1")
            self.driver.find_element(By.XPATH, "//input[@id='billing:firstname']").send_keys("Miastowe")

            # odbior osobisty
            self.driver.find_element(By.CSS_SELECTOR, "label[for='s_method_flatrate_flatrate']").click()
            # metodia platnosci
            self.driver.find_element(By.XPATH, "//input[@id='p_method_banktransfer']").click()

            # potwierdzenie zamówienia
            time.sleep(5)
            self.driver.find_element(By.XPATH, "//span[normalize-space()='Potwierdzam zamówienie']").click()
            time.sleep(5)
            if self.driver.current_url == "https://dev321.seart.pl/onepagecheckout/index/success/":
                self.ass = True
            else:
                self.ass = False
            self.assertTrue(self.ass, "cos poszlo nie tak")
            if self.counter == len(self.urls):
                self.driver.close()
            else:
                continue

            self.counter += 1

    def tearDown(self):
        time.sleep(2)
        self.driver.quit()


if __name__ == "__main__":
    unittest.main()
# //span[normalize-space()='Potwierdzam zamówienie']
