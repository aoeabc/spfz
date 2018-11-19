from util.ObjectMap import *


class FkrwfktzPage:
    def __init__(self, driver):
        self.driver = driver

    def queryBtnObj(self):
        # 查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='query();']")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtzBtnObj(self, narid = None):
        # 调整按钮
        if narid != None:
            try:
                elementObj = getElement(self.driver, "xpath", "//td[contains(text(),\'"+narid+"\')]/following-sibling::td[7]/a[1]")
                return elementObj
            except Exception as e:
                raise e

        else:
            try:
                elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,'openTask')]")
                return elementObj
            except Exception as e:
                raise e
    def nsrsbhObj(self):
        # 调整页面，获取纳税人识别号
        try:
            elementObj = getElement(self.driver, "id", "nsrsbhTd")
            return elementObj
        except Exception as e:
            raise e

    def sfsjssObj(self, check = None):
        # 是否涉及税收
        if check == None or check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "id", "mini-33$ck$0")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "id", "mini-33$ck$1")
                return elementObj
            except Exception as e:
                raise e

    def sfwflxObj(self, check = None):
        # 任务反馈页面，是否无法联系单选框
        if check == None or check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '是否无法联系')]"
                                                              "/following-sibling::td[1]/div/div/div[1]/input")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '是否无法联系')]"
                                                              "/following-sibling::td[1]/div/div/div[2]/input")
                return elementObj
            except Exception as e:
                raise e

    def sfjbphObj(self, check = None):
        # 任务反馈页面，是否拒不配合单选框
        if check == None or check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '是否拒不配合')]"
                                                              "/following-sibling::td[1]/div/div/div[1]/input")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '是否拒不配合')]"
                                                              "/following-sibling::td[1]/div/div/div[2]/input")
                return elementObj
            except Exception as e:
                raise e

    def bzzcdzjx(self, check = None):
        # 任务反馈页面，经实地核查不在注册地经营单选框
        if check == None or check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '经实地核查不在注册地经营')]"
                                                              "/following-sibling::td[1]/div/div/div[1]/input")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "xpath", "//th[contains(text(), '经实地核查不在注册地经营')]"
                                                              "/following-sibling::td[1]/div/div/div[2]/input")
                return elementObj
            except Exception as e:
                raise e

    def pzhdCheckboxObj(self):
        # 票种核定勾选框
        try:
            elementObj = getElement(self.driver, "id", "pzhd")
            return elementObj
        except Exception as e:
            raise e

    def fplgCheckboxObj(self):
        # 发票领购勾选框
        try:
            elementObj = getElement(self.driver, "id", "fplg")
            return elementObj
        except Exception as e:
            raise e

    def zgswjgbgCheckboxObj(self):
        # 主管税务机关变更勾选框
        try:
            elementObj = getElement(self.driver, "id", "zgswjgbg")
            return elementObj
        except Exception as e:
            raise e

    def nsrsfywtObj(self, check = None):
        # 任务反馈页面，纳税人是否有无问题
        if check == None or check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "id", "mini-181$ck$1")
                return elementObj
            except Exception as e:
                raise e

        elif check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "id", "mini-181$ck$0")
                return elementObj
            except Exception as e:
                raise e

    def ydgzqksmObj(self):
        # 应对工作情况说明输入框
        try:
            elementObj = getElement(self.driver, "id", "pgzxqk$text")
            return elementObj
        except Exception as e:
            raise e

    def rwtjBtnObj(self):
        # 任务反馈页面，提交按钮
        try:
            elementObj = getElement(self.driver, "id", "bc")
            return elementObj
        except Exception as e:
            raise e

    def rwfktjMessageBtnObj(self):
        # 是否反馈提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def fkMessageBtnObj(self):
        # 分配成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'确定')]")
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

