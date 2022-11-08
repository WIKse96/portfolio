import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class ProdPage:

    def __init__(self, driver, productList):

        self.driver = driver
        self.productList = productList

    def signUp(self):
        lenPL = len(self.productList)
        counter = 0
        for productCard in self.productList:
            productCard.click()
            self.driver.find_element(By.XPATH, "//input[@id='email-notification']").send_keys("test@seart.pl")
            self.driver.find_element(By.XPATH, "//input[@value='Powiadom o dostępności']").click()
            self.driver.execute_script("window.history.go(-1)")
            # counter =+1
            # if counter == lenPL:
            #     break
        time.sleep(2)
        return True
