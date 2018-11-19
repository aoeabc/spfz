from pageObjects.LoginPage import LoginPage
from selenium import webdriver


class LoginAction:
    def __init__(self):
        print("login.......")

    @staticmethod
    def login(driver, username, password):
        try:
            login = LoginPage(driver)
            login.userNameObj().clear()
            login.userNameObj().send_keys(username)
            login.passWordObj().send_keys(password)
            login.loginBtnObj().click()
        except Exception as e:
            raise e

    @staticmethod
    def driver(url):
        try:
            bro = webdriver.Ie()
            bro.get(url)
            handles = bro.window_handles
            bro.switch_to.window(handles[0])
            bro.implicitly_wait(30)
            return bro

        except Exception as e:
            raise e

if __name__=='__main__':
    l = LoginAction()
    driver = l.driver('http://86.100.16.15:8001')
    l.login(driver, 'szgsfengyj', '888888')