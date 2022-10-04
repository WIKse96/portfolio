import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


class TestNotifi(unittest.TestCase):

    def setUp(self):
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors"])
        self.options.add_argument("window-size=1900,1050")
        self.options.add_argument('headless')
        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.driver = webdriver.Chrome(service=self.serviceObj, options=self.options)
        # self.assertIn("Akcesoria, uchwyty, okucia meblowe - RustykalneUchwyty.pl", self.driver.title)
        self.driver.implicitly_wait(5)

    def test_OrderSimpleProduct(self):
        self.driver.get("https://vu2005.admin.s37.mhost.eu/uchwyt-sufitowy-lampy-z-lancuchem.html")

        try:
            sendNot = self.driver.find_element(By.CSS_SELECTOR, "input[value='Powiadom o dostępności']")
        except:
            print("!!Produkt nie spełnia wymagań!!", self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message").text)
            self.driver.quit()

        # klikam w pusty
        sendNot.click()
        # sprawdzam walidację pustego formularza
        self.assertTrue(self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message"))
        self.driver.find_element(By.CSS_SELECTOR, "#email-notification").send_keys("test@seart.pl")
        sendNot.click()
        time.sleep(2)

        el = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CSS_SELECTOR,"#notyfication-message"))
        )

        self.assertTrue(el.text == "Twój email został dodany", "email już dodany")
        print(self.driver.find_element(By.CSS_SELECTOR, "#notyfication-message").text)


    def tearDown(self):

        self.driver.quit()


if __name__ == "__main__":
    unittest.main()

