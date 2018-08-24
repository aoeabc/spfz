from util.ObjectMap import *

class LoginPage:
    def __init__(self,driver):
        self.driver=driver

    def userNameObj(self):
        try:
            elementObj=getElement(self.driver,"id","username")
            return elementObj
        except Exception as e:
            raise e

    def passWordObj(self):
        try:
            elementObj=getElement(self.driver,"id","password")
            return elementObj
        except Exception as e:
            raise e
    def loginBtnObj(self):
        try:
            elementObj=getElement(self.driver,"id","loginBtn")
            return elementObj
        except Exception as e:
            raise e
