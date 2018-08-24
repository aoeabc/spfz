from util.ObjectMap import *

class HmdrdPage:
    def __init__(self,driver):
        self.driver=driver


    def nullMessageBtnObj(self):
        #登录后没有菜单时弹出一个“null”的提示框,点确定按钮，不确定回弹出几个，一直点 。
        try:
            elementObj=getElement(self.driver,"xpath","//div[@class='mini-messagebox-buttons']/a[@id='mini-29']")
            return elementObj
        except Exception as e:
            raise e