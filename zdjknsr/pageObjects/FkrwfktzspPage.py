from util.ObjectMap import *


class FkrwfktzspPage:
    def __init__(self, driver):
        self.driver = driver

    def queryBtnObj(self):
        # 查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='query();']")
            return elementObj
        except Exception as e:
            raise e

    def tzspBtnObj(self, narid = None):
        # 审批按钮
        if narid == None:
            try:
                elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,'javascript:sp')]")
                return elementObj
            except Exception as e:
                raise e
        else:
            try:
                elementObj = getElement(self.driver, "xpath", "//td[contains(text(),\'"+narid+"\')]/following-sibling::td[7]/a[1]")
                return elementObj
            except Exception as e:
                raise e


    def tzspjgObj(self, tag = None):
        # 反馈复核结果,同意或者不同意
        if tag == "n" or tag == "N" or tag == "否" or tag == "不同意":
            try:
                elementObj = getElement(self.driver, "id", "mini-5$ck$1")
                return elementObj
            except Exception as e:
                raise e

        elif tag == "y" or tag == "Y" or tag == "是" or tag == "同意" or tag == None:
            try:
                elementObj = getElement(self.driver, "id", "mini-5$ck$0")
                return elementObj
            except Exception as e:
                raise e

    def spyjsmObj(self):
        # 审批意见说明
        try:
            elementObj = getElement(self.driver, "id", "spyj$text")
            return elementObj
        except Exception as e:
            raise

    def spbcObj(self):
        # 调整审批保存按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='doBc()']")
            return elementObj
        except Exception as e:
            raise

    def tjspMessageBtnObj(self):
        # 复核成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def tjMessageObj(self):
        # 保存后的提示信息，用innerText属性获取
        try:
            elementObj = getElement(self.driver, "xpath", "//td[@class='mini-messagebox-content-text']")
            return elementObj
        except Exception as e:
            raise e