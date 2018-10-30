from util.ObjectMap import *


class FkrwfpPage:
    def __init__(self, driver):
        self.driver = driver

    def queryBtnObj(self):
        # 查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='FormOp.doQuery();']")
            return elementObj
        except Exception as e:
            raise e

    def rwfpBtnObj(self, rwbh):
        # 分配按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(text(),\'"+rwbh+"\')]/../following-sibling::td[11]/a[1]")
            return elementObj
        except Exception as e:
            raise e

    def ydryBtnObj(self):
        # 分配页面应对处置人员选择
        try:
            # exp="mini-170$"+num
            exp = "mini-170$0"
            elementObj = getElement(self.driver, "xpath", "//tr[@id=\'" + exp + "\']/td[10]")
            return elementObj
        except Exception as e:
            raise e

    def ydrySltBtnObj(self):
        # 分配页面应对处置人员下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-90']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def ydryqueryObj(self):
        # 分配页面应对处置人员框，查询输入框。
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-93']/span/input")
            return elementObj
        except Exception as e:
            raise e

    def ydryqueryBtnObj(self):
        # 分配页面应对处置人员框，查询按钮。
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-94']/span")
            return elementObj
        except Exception as e:
            raise e

    def ydryObj(self, ydryname):
        # 分配页面应对处置人员框，选择应对人员。
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@class='mini-tree-nodetext' and contains(text(),\'" + ydryname + "\')]")
            return elementObj
        except Exception as e:
            raise e

    def qrfqBtnObj(self):
        # 分配页面确认分配按钮。
        try:
            elementObj = getElement(self.driver, "id", "qrfp_btn")
            return elementObj
        except Exception as e:
            raise e