from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from time import sleep



class MakeOrder:
    def __init__(self, websiteToTest):
        self.actualURL = None
        self.websiteToTest = websiteToTest


        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serviceObj)

    def makeOrder(self):
        self.driver.get(self.websiteToTest)
        self.driver.maximize_window()
        self.driver.find_element(By.CLASS_NAME, "btn-cart").click()
        self.driver.get("https://dev321.seart.pl/checkout/cart/")
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/fieldset[1]/table[1]/tbody[1]/tr[1]/td[5]/input[1]").clear()
        self.driver.find_element(By.XPATH, "/html[1]/body[1]/div[1]/div[1]/div[9]/div[1]/div[1]/div[1]/div[2]/div[1]/form[1]/fieldset[1]/table[1]/tbody[1]/tr[1]/td[5]/input[1]").send_keys("2")
        self.driver.find_element(By.XPATH, "//button[@title='Aktualizuj koszyk']").click()
        self.driver.find_element(By.XPATH, "//div[@class='totals']//ul[@class='checkout-types']//li//button[@title='Przejdź do kasy']//span//span[contains(text(),'Przejdź do kasy')]").click()
        self.driver.find_element(By.XPATH, "//input[@id='billing:firstname']").send_keys("Automat")
        self.driver.find_element(By.XPATH, "//input[@id='billing:lastname']").send_keys("TEST")
        self.driver.find_element(By.XPATH, "//input[@placeholder='nazwa@domena.pl']").send_keys("TEST@seart.pl")
        self.driver.find_element(By.XPATH, "//input[@id='billing:telephone']").send_keys("791111111")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street1']").send_keys("791111111")
        self.driver.find_element(By.XPATH, "//input[@id='billing:street2']").send_keys("7")
        self.driver.find_element(By.XPATH, "//input[@id='billing:floor']").send_keys("55-555")
        self.driver.find_element(By.XPATH, "//input[@id='billing:postcode']").send_keys("55-555")
        self.driver.find_element(By.XPATH, "//input[@id='billing:city']").send_keys("miasto")
        self.driver.find_element(By.XPATH, "//input[@id='s_method_freeshipping_freeshipping']").click()
        self.driver.find_element(By.XPATH, "//input[@id='p_method_banktransfer']").click()
        self.driver.find_element(By.XPATH, "//input[@id='agreement-1']").click()
        self.driver.find_element(By.XPATH, "//input[@id='agreement-3']").click()
        sleep(6)
        self.driver.find_element(By.XPATH, "//button[@title='Potwierdzam zamówienie']").click()
        print(self.driver.current_url)
        self.driver.close()




# obj = MakeOrder('https://dev321.seart.pl/biurko-sosnowe-woskowane-rustyk.html').makeOrder()
# obj.makeOrder()