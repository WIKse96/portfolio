from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class TryLogin:

    def __init__(self, idUser, loginEmail, loginPass, nickName, counter, websiteToTest, accountUrl, lenghtOfLoginDatas):

        self.id = idUser
        self.loginEmail = loginEmail
        self.loginPass = loginPass
        self.nickName = nickName
        self.websiteToTest = websiteToTest
        self.accountUrl = accountUrl
        self.serviceObj = Service("E:/Wiktor/inne/py/selenium/chromedriver/chromedriver.exe")
        self.loginPath = ''
        self.message = None
        self.counter = counter
        self.lenghtOfLoginDatas = lenghtOfLoginDatas
        self.driver = webdriver.Chrome(service=self.serviceObj)

    def login(self):


        self.driver.get(self.websiteToTest)
        #złapanie lementu zaloguj
        self.driver.find_element(By.XPATH, "//a[@title='Zaloguj']").click()

        self.loginPath = self.driver.current_url
        #złapanie pól do logowania
        self.driver.find_element(By.ID, "email").send_keys(self.loginEmail)
        self.driver.find_element(By.ID, "pass").send_keys(self.loginPass)

        #klik wyślij
        self.driver.find_element(By.ID, "send2").click()
        if self.loginPath == self.driver.current_url:
            print("Błędne hasło lub login")
            print(f"email:{self.loginEmail}")
            print(f"hasło:{self.loginPass}")
        elif self.accountUrl == self.driver.current_url:
            print("Dostęp przyznany - zalogowano")
            print(f"użytkownik: {self.loginEmail}")
            print(self.driver.current_url)
            self.message = self.driver.find_element(By.CLASS_NAME, "welcome-msg").text
        else:
            print("cos jest źle")

        #zamykanie okna po ostatnim logowaniu
        if self.counter == self.lenghtOfLoginDatas:
            self.driver.close()
        else:
            pass
        #sprawdzenie poprawności logowania
        assert f"{self.nickName}" in self.message
