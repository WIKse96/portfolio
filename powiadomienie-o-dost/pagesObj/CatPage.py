import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class CatPage:

    def __init__(self, driver):
        self.driver = driver

    allProducts = (By.XPATH, "//div[@class='category-products'] // li[contains(@class,'item')]/div/div")
    testprod = (By.XPATH, "//img[@alt='RustykalneUchwyty.pl']")

    def getAllGroupedToNotifi(self):
        productToTest = []
        for product in (self.driver.find_elements(*CatPage.allProducts)):
            if product.find_element(By.XPATH, "//div[@class='description-wrapper']/div[@class='btn-border btn-border-product-list']"):
                productToTest.append(product)
        print('CatPage.productToTest**', productToTest)
        return productToTest
