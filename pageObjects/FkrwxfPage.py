from util.ObjectMap import *


class FkrwxfPage:
    def __init__(self, driver):
        self.driver = driver

    def queryBtnObj(self):
        # 查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='query();']")
            return elementObj
        except Exception as e:
            raise e

    def rwxfSltBtn(self, rwbh):
        # 勾选框
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(text(),\'"+rwbh+"\')]/../preceding-sibling::td[1]/input")
            return elementObj
        except Exception as e:
            raise e

    def plxfBtn(self):
        # 批量下发按钮
        try:
            elementObj = getElement(self.driver, "id", "plxf")
            return elementObj
        except Exception as e:
            raise e

    def plxfMessageBtnObj(self):
        # 批量下发提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-72']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def tjMessageObj(self):
        # 提交审批后的提示信息，用innerText属性获取
        try:
            elementObj = getElement(self.driver, "xpath", "//td[@class='mini-messagebox-content-text']")
            return elementObj
        except Exception as e:
            raise e

    def xfMessageBtnObj(self):
        # 下发成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-75']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e