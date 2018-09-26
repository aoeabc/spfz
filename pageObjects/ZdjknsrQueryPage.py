from util.ObjectMap import *


class ZdjknsrQueryPage:
    def __init__(self, driver):
        self.driver = driver


    def dateFrameObj(self):
        # 时间控件
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@id='_my97DP']/iframe")
            return elementObj
        except Exception as e:
            raise e

    def nsrsbhObj(self):
        try:
            elementObj=getElement(self.driver,"xpath","//input[@id='nsrsbh$text')]")
            return elementObj
        except Exception as e:
            raise e

    def nsrmcObj(self):
        try:
            elementObj=getElement(self.driver,"xpath","//input[@id='nsrmc$text')]")
            return elementObj
        except Exception as e:
            raise e

    def pcbhObj(self):
        # 批次编号
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@id='pcbh$text']")
            return elementObj
        except Exception as e:
            raise e

    def tjsjqObj(self):
        # 提交时间起
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='tjsjq')]//sapn[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def tjsjzObj(self):
        # 提交时间止
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='tjsjz')]//sapn[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def timeDateObj(self):
        # 时间选择“日”
        try:
            elementObj = getElement(self.driver, "xpath", "//td[contains(text(),'11')]")
            return elementObj
        except Exception as e:
            raise e

    def jklxObj(self):
        # 监控类型下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='jklx']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def jklxCbObj(self):
        # 监控类型下拉框内容
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@id='mini-6$ck$1']")
            return elementObj
        except Exception as e:
            raise e

    def xzjklxCbObj(self,lx):
        # 新增页面监控类型下拉框内容
        try:
            exp="\'"+lx+"\'"
            elementObj = getElement(self.driver, "xpath", "//td[contains(text(),"+exp+")]")
            return elementObj
        except Exception as e:
            raise e


    def queryBtnObj(self):
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@type='button']")
            return elementObj
        except Exception as e:
            raise e

    def resetBtnObj(self):
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@type='reset']")
            return elementObj
        except Exception as e:
            raise e

    def checkboxObj(self,id):
        try:
            elementObj = getElement(self.driver, "id", id)
            return elementObj
        except Exception as e:
            raise e