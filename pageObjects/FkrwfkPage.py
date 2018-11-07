from util.ObjectMap import *


class FkrwfkPage:
    def __init__(self, driver):
        self.driver = driver

    def queryBtnObj(self):
        # 定义页面查询按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@name='B15']")
            return elementObj
        except Exception as e:
            raise e

    def rwfkBtnObj(self, rwbh):
        # 任务反馈按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//td[contains(text(),\'"+rwbh+"\')]/following-sibling::td[8]/a[1]")
            return elementObj
        except Exception as e:
            raise e

    def ksfkBtnObj(self):
        # 应对反馈页面，开始反馈按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@herf,'javascript:doFk')]")
            return elementObj
        except Exception as e:
            raise e

    def sfwflxObj(self, check):
        # 任务反馈页面，是否无法联系单选框
        if check == "n" or check == "N" or check == "否":
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

    def sfjbphObj(self, check):
        # 任务反馈页面，是否拒不配合单选框
        if check == "n" or check == "N" or check == "否":
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

    def bzzcdzjx(self, check):
        # 任务反馈页面，经实地核查不在注册地经营单选框
        if check == "n" or check == "N" or check == "否":
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

    def zgswjgbgCheckboxObj(self):
        # 主管税务机关变更勾选框
        try:
            elementObj = getElements(self.driver, "id", "zgswjgbg")
            return elementObj
        except Exception as e:
            raise e