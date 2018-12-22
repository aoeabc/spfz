from util.ObjectMap import *


class FkrwfkfhPage:
    def __init__(self, driver):
        self.driver = driver

    def rwlxradioObj(self):
        # 查询条件任务类型
        try:
            elementObj = getElement(self.driver, "id", "mini-40$ck$0")
            return elementObj
        except Exception as e:
            raise e

    def queryBtnObj(self):
        # 定义页面查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@name='B15']")
            return elementObj
        except Exception as e:
            raise e

    def fkfhBtnObj(self, rwid = None):
        # 复核按钮
        if rwid != None:
            try:
                elementObj = getElement(self.driver, "xpath", "//a[contains(@href,\'"+rwid+"\')]")
                return elementObj
            except Exception as e:
                raise
        else:
            try:
                elementObj = getElement(self.driver, "xpath", "//a[contains(@href,'javascript:doSp')]")
                return elementObj
            except Exception as e:
                raise


    def fkfhjgObj(self, tag = None):
        # 反馈复核结果,同意或者不同意
        if tag == "n" or tag == "N" or tag == "否" or tag == "不同意":
            try:
                elementObj = getElement(self.driver, "id", "mini-24$ck$1")
                return elementObj
            except Exception as e:
                raise e

        elif tag == "y" or tag == "Y" or tag == "是" or tag == "同意" or tag == None:
            try:
                elementObj = getElement(self.driver, "id", "mini-24$ck$0")
                return elementObj
            except Exception as e:
                raise e

    def fkfhsmObj(self):
        # 反馈复核说明
        try:
            elementObj = getElement(self.driver, "id", "spyjsm$text")
            return elementObj
        except Exception as e:
            raise

    def fkfhbcObj(self):
        # 反馈复核保存按钮
        try:
            elementObj = getElement(self.driver, "id", "bc")
            return elementObj
        except Exception as e:
            raise

    def fkfhMessageBtnObj(self):
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