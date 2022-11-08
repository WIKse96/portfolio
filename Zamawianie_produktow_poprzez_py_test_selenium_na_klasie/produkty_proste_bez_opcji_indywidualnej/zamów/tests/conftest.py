import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import pytest


# funkcja odpowiada za konsole. defaultowo jest chrome, moge podac inną przeglądarkę
def pytest_addoption(parser):
    parser.addoption(
        "--product_url"
        "", action="store", default="https://vu2005.admin.s37.mhost.eu/dekoracja-scienna-metalowa-3d-loft-band.html",
    )


# oznaczenie, że poniższa funkcja jest w scope klasy
@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    # pobranie tego co zostało wpisane w konsole
    product_url = request.config.getoption("product_url")
    options.add_argument('headless')
    serviceObj = Service("E:/Wiktor/py/selenium/chromedriver/chromedriver.exe")
    driver = webdriver.Chrome(service=serviceObj, options=options)
    # zadeklarowanie driver w taki sposób aby przekazać go do innego pliku
    driver.get(product_url)
    driver.set_window_rect(width=1200, height=900)
    request.cls.driver = driver
    # tutaj wykonują się testy, yield to oznacza
    yield
    # po wszystkim na koniec przegladarka się zamyka
    driver.close()
