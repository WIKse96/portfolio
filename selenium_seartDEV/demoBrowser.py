from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://www.seart.pl/")
print(driver.title)
print(driver.current_url)

print(driver.get_screenshot_as_png())
# driver.close()
