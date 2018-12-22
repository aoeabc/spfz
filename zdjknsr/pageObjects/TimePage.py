from util.ObjectMap import *


class TimePage:
    def __init__(self, driver):
        self.driver = driver

    def dateFrameObj(self):
        # 时间控件框架
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@id='_my97DP']/iframe")
            return elementObj
        except Exception as e:
            raise e

    def dateEnterBtnObj(self):
        # 时间控件确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@class='yminputfocus']")
            return elementObj
        except Exception as e:
            raise e

    def dateOKBtnObj(self):
        # 时间控件确定按钮
        try:
            elementObj = getElement(self.driver, "id", "dpOkInput")
            return elementObj
        except Exception as e:
            raise e

    def dateSectBtnObj(self,id):
        # 弹出时间控件按钮
        try:
            elementObj = getElement(self.driver, "css selector", "span#"+id+">span>span>span>span.mini-buttonedit-icon")
            return elementObj
        except Exception as e:
            raise e

    def timeYearObj(self):
        # 时间选择“年”
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@class='menuSel YMenu']/following-sibling::input[1]")
            return elementObj
        except Exception as e:
            raise e

    def timeMonthObj(self):
        # 时间选择“月”
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@class='menuSel MMenu']/following-sibling::input[1]")
            return elementObj
        except Exception as e:
            raise e

    def timeDateObj(self, year, mouth, date):
        # 时间选择“日”
        try:
            exp=year+','+mouth+','+date
            elementObj = getElement(self.driver, "xpath", "//td[contains(@onclick,'("+exp+")')]")
            return elementObj
        except Exception as e:
            raise e