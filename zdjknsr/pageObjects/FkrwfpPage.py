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
            # exp="mini-17$"+num
            exp = "mini-17$0"
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

    def rwfpcheckObj(self):
        # 分配页面勾选框
        try:
            # exp="mini-17$"+num
            exp = "mini-17$0"
            elementObj = getElement(self.driver, "xpath", "//tr[@id=\'" + exp + "\']/td[1]/input")
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

    def rwfpMessageBtnObj(self):
        # 是否分配提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-99']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def fpMessageBtnObj(self):
        # 分配成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-102']/span[contains(text(),'确定')]")
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

    def fpfhMessageBtnObj(self):
        # 分配成功后，已经没有需要分配的信息，提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-91']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e