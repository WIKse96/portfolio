import time

from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass
from pagesObj.CatPage import CatPage
from pagesObj.ProdPage import ProdPage

# @pytest.mark.usefixtures("setup") - dziedziczone z BaseClass
class TestOne(BaseClass):

    def test_e2e(self, setup):
        #przeskrolowanie w celu załadowania lisitngu
        self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #przejście do kategorii
        category = CatPage(self.driver)
        productsToTestList = category.getAllGroupedToNotifi()
        productCard = ProdPage(self.driver,productsToTestList)
        counter = 0
        while counter < 5:
            productsToTestList[counter].click()
            self.driver.find_element(By.XPATH, "//input[@id='email-notification']").send_keys("test@seart.pl")
            time.sleep(2)
            self.driver.find_element(By.XPATH, "//input[@value='Powiadom o dostępności']").click()
            time.sleep(2)
            counter+=1
            self.driver.execute_script("window.history.go(-1)")
        # productCard.signUp()


