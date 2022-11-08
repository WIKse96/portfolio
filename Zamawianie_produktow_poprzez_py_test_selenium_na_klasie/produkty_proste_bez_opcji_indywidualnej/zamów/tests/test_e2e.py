import pytest
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from utilities.BaseClass import BaseClass


# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestUnloggedSimple(BaseClass):

    def test_notLogged(self, setup):
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.XPATH, "//button[@class='button big btn-cart']").click()
        time.sleep(4)
        action = ActionChains(self.driver)
        action.move_to_element(self.driver.find_element(By.CSS_SELECTOR, ".napis-koszyk")).perform()
        self.driver.find_element(By.XPATH, "//button[@title='Zamówienie']").click()

        self.driver.find_element(By.XPATH, "//input[@id='billing:firstname']").send_keys("Wiktor")
        self.driver.find_element(By.XPATH, "//input[@id='billing:lastname']").send_keys("Testowy")
        self.driver.find_element(By.XPATH, "//input[@placeholder='nazwa@domena.pl']").send_keys("test@seart.pl")
        self.driver.find_element(By.XPATH, "//input[@id='billing:telephone']").send_keys("998747474")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street1']").send_keys("testowa ulica")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street2']").send_keys("23a")
        self.driver.find_element(By.XPATH, "//input[@id='billing:postcode']").send_keys("25-555")
        self.driver.find_element(By.XPATH, "//input[@id='billing:city']").send_keys("Chmielnik")
        self.driver.find_element(By.XPATH, "//img[@id='odbiorosobistybtn']").click()
        self.driver.find_element(By.XPATH, "//img[@id='codbtn']").click()
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//input[@id='agreement-3']").click()
        self.driver.find_element(By.XPATH, "//input[@id='agreement-5']").click()
        time.sleep(3)
        self.driver.find_element(By.XPATH, "//button[@title='Potwierdzam zamówienie']").click()
        print(self.driver.find_element(By.CSS_SELECTOR, "h2[class='title'] span").text)
        assert "onepagecheckout/index/success/" in self.driver.current_url
