from OpenFileWithData import OpenFileWithData
from seartDEV_TryLogin import TryLogin
from seartDEV_makeOrder import MakeOrder

path = OpenFileWithData("login.json")

loginInJSON = path.open()

websiteToTest = 'https://dev321.seart.pl/'
accountUrl = 'https://dev321.seart.pl/customer/account/'

lenghtOfLoginDatas = len(loginInJSON['loginDatas'])


def datasFromJson():
    counter = 1
    for loginData in loginInJSON['loginDatas']:
        email = loginData['loginEmail']
        loginPass = loginData['loginPass']
        nickName = loginData['nickName']
        testDatas = TryLogin(1, email, loginPass, nickName, counter, websiteToTest, accountUrl, lenghtOfLoginDatas)
        if counter == 1:

            #skladanie zamówienia
            MakeOrder('https://dev321.seart.pl/biurko-sosnowe-woskowane-rustyk.html').makeOrder()
            print("counter", counter)
        else:
            pass
        counter += 1
        testDatas.login()


datasFromJson()
