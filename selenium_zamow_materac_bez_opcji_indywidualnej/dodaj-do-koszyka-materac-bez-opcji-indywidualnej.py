import time

from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=serviceObj)

websiteToTest = 'https://www.seart.pl/'
driver.get(websiteToTest)
driver.maximize_window()
search= driver.find_element(By.CSS_SELECTOR, "body > div:nth-child(2) > div:nth-child(2) > div:nth-child(4) > div:nth-child(2) > div:nth-child(1) > div:nth-child(1) > div:nth-child(4) > form:nth-child(1) > div:nth-child(1) > input:nth-child(3)")
search.send_keys("materac")
search.send_keys(Keys.ENTER)

productCards = driver.find_elements(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(2) > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > ul:nth-child(4) > li>div>div.description-wrapper>h2>a")

for productCard in productCards:
    if driver.find_element(By.CSS_SELECTOR,"body > div:nth-child(3) > div:nth-child(2) > div:nth-child(10) > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(5) > ul:nth-child(4) > li>div>div.description-wrapper>div.actions>button").get_attribute("title") == "Do koszyka":
        productCard.click()
        break
driver.find_element(By.CSS_SELECTOR,"button[title='Do koszyka'] span span").click()
time.sleep(3)
assert driver.find_element(By.XPATH,"//span[@class='items']").text

driver.close()

