import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
import pytest
from webdriver_manager.core.utils import ChromeType


# funkcja odpowiada za konsole. defaultowo jest chrome, moge podac inną przeglądarkę
def pytest_addoption(parser):
    parser.addoption(
        "--cat_url"
        "", action="store", default="https://vu2005.admin.s37.mhost.eu/127-systemy-drzwi-przesuwnych",
    )


# oznaczenie, że poniższa funkcja jest w scope klasy
@pytest.fixture(scope="class")
def setup(request):
    options = webdriver.ChromeOptions()
    # pobranie tego co zostało wpisane w konsole
    cat_url = request.config.getoption("cat_url")
    # options.add_argument('headless')
    driver = webdriver.Chrome(ChromeDriverManager(chrome_type=ChromeType.CHROMIUM).install())

    # zadeklarowanie driver w taki sposób aby przekazać go do innego pliku
    driver.get(cat_url)
    driver.fullscreen_window()
    driver.implicitly_wait(3)
    request.cls.driver = driver
    # tutaj wykonują się testy, yield to oznacza
    yield

    # po wszystkim na koniec przegladarka się zamyka
    driver.close()
