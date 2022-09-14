from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service_obj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
driver = webdriver.Chrome(service=service_obj)
driver.get("https://dev321.seart.pl/")
print(driver.title)
print(driver.current_url)
# driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
# driver.maximize_window()
# driver.back()
# driver.refresh()
# driver.forward()
# print(driver.title)
print(driver.get_screenshot_as_png())
# driver.close()
