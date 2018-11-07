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
            elementObj = getElement(self.driver, "xpath", "//a[contains(@href,'javascript:doFk')]")
            return elementObj
        except Exception as e:
            raise e

    def sfsjssObj(self, check):
        # 任务反馈页面，是否涉及税收
        if check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "id", "mini-32$ck$0")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "id", "mini-32$ck$1")
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

    # 查补情况节点,不涉及税收时 ，这部分在页面不显示--------------------------------------------------------------
    def zgswjgbgCheckboxObj(self,num):
        # 查补情况表格点击
        num1 = num-1
        exp = "mini-60$0$"+str(num1)
        try:
            elementObj = getElements(self.driver, "id", exp)
            return elementObj
        except Exception as e:
            raise e

    def zsxmSltBtnObj(self):
        # 征收项目下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-197']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def zsxmSltObj(self):
        # 征收项目下拉框内容
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@id='mini-204$1']//span[@class='mini-tree-nodetext']")
            return elementObj
        except Exception as e:
            raise e

    def zspmSltBtnObj(self):
        # 征收品目下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-205']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def zspmSltObj(self):
        # 征收品目下拉框内容
        try:
            elementObj = getElement(self.driver, "xpath", "")
            return elementObj
        except Exception as e:
            raise e

    #------------------------------------------------------------------------------------------------
    def nsrsfywtObj(self, check):
        # 任务反馈页面，纳税人是否有无问题
        if check == "n" or check == "N" or check == "否":
            try:
                elementObj = getElement(self.driver, "id", "mini-181$ck$0")
                return elementObj
            except Exception as e:
                raise e

        elif check == "y" or check == "Y" or check == "是":
            try:
                elementObj = getElement(self.driver, "id", "mini-181$ck$1")
                return elementObj
            except Exception as e:
                raise e

    def ydgzqksmObj(self):
        # 任务反馈页面，应对工作情况说明输入框
        try:
            elementObj = getElement(self.driver, "id", "pgzxqk$text")
            return elementObj
        except Exception as e:
            raise e

    def rwtjBtnObj(self):
        # 任务反馈页面，提交按钮
        try:
            elementObj = getElement(self.driver, "id", "rwtj")
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
