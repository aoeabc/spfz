from util.ObjectMap import *
from conf.ParseConfigurationFile import ParseConfigFile

class LoginPage:

    def __init__(self,driver):
        self.driver=driver
        self.config = ParseConfigFile()
        self.option = self.config.getItemsSection("LoginPage")

    def userNameObj(self):
        try:
            locateType, locateExpression = self.option["LoginPage.userNameObj".lower()].split(">")
            elementObj = getElement(self.driver,locateType,locateExpression)
            return elementObj
        except Exception as e:
            raise e

    def passWordObj(self):
        try:
            locateType, locateExpression = self.option["LoginPage.passWordObj".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locateExpression)
            return elementObj
        except Exception as e:
            raise e

    def loginBtnObj(self):
        try:
            locateType, locateExpression = self.option["LoginPage.loginBtnObj".lower()].split(">")
            elementObj = getElement(self.driver, locateType, locateExpression)
            return elementObj
        except Exception as e:
            raise e
