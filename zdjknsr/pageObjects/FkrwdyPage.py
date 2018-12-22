from util.ObjectMap import *


class FkrwdyPage:
    def __init__(self, driver):
        self.driver = driver

    def rwdyBtnObj(self):
        # 批次页面任务定义按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@onclick='dorwdy()']")
            return elementObj
        except Exception as e:
            raise e

    def bcBtnObj(self):
        # 定义页面保存按钮
        try:
            elementObj = getElement(self.driver, "id", "bc")
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

    def rwpcmcObj(self):
        # 定义页面任务批次名称输入框
        try:
            elementObj = getElement(self.driver, "id", "rwpc_ms$text")
            return elementObj
        except Exception as e:
            raise e

    def tableclickObj(self, name, num=1):
        # 定义页面后续处理、接收机关、应对方式，选择对应的输入框
        exp = "mini-160$" + str(num)
        # exp = "mini-160$0"
        if name=="后续处理":
            try:
                elementObj = getElement(self.driver, "xpath", "//tr[@id=\'"+exp+"\']/td[9]")
                return elementObj
            except Exception as e:
                raise e

        elif name=="接收机关":
            try:
                elementObj = getElement(self.driver, "xpath", "//tr[@id=\'"+exp+"\']/td[10]")
                return elementObj
            except Exception as e:
                raise e

        elif name=="应对方式":
            try:
                elementObj = getElement(self.driver, "xpath", "//tr[@id=\'"+exp+"\']/td[11]")
                return elementObj
            except Exception as e:
                raise e

        elif name=="勾选框":
            try:
                elementObj = getElement(self.driver, "xpath", "//tr[@id=\'"+exp+"\']/td[1]/input")
                return elementObj
            except Exception as e:
                raise e

    def hxclBtnObj(self):
        # 定义页面后续处理框下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-218']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def jsjgBtnObj(self):
        # 定义页面接收机关框下拉框按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='ydjg']//span[@class='mini-buttonedit-icon']")
            return elementObj
        except Exception as e:
            raise e

    def hxclSltObj(self, hxcl):
        # 定义页面后续处理框下拉框内容
        try:
            elementObj = getElement(self.driver, "xpath", "//td[contains(text(),\'"+hxcl+"\')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgSltObj(self,ydjg):
        # 定义页面应对机关菜单树内容
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@id='ydjg']//span[contains(text(),\'"+ydjg+"\')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtreeBtnObj(self):
        # 定义页面应对机关菜单树确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@class='bottombutton_1']")
            return elementObj
        except Exception as e:
            raise e

    def rwwcqxBtnObj(self):
        # 定义页面任务完成期限确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@id='rwwcsx_window']//span[contains(text(),'确定')]")
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

    def bcMessageBtnObj(self):
        # 保存成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-224']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def fbMessageBtnObj(self):
        # 发布成功提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@id='mini-46']/span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfbBtnObj(self, pcmc):
        # 列表中发布按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@href,\'"+pcmc+"\')]/following-sibling::a[2]")
            return elementObj
        except Exception as e:
            raise e

    def zjfbBtnObj(self):
        # 直接发布按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[contains(@onclick,'dozjfb')]")
            return elementObj
        except Exception as e:
            raise e
