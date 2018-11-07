from util.ObjectMap import *


class TreePage:
    def __init__(self, driver):
            self.driver = driver

    def mainTreeFrameObj(self):
        # 主页面菜单区域
        try:
            elementObj = getElement(self.driver,"xpath","//iframe[contains(@src,'tab_index.html')]")
            return elementObj
        except Exception as e:
            raise e

    def thirdTreeFrameObj(self):
        # 第三级菜单页面的最外层，可以选择第三级菜单
        try:
            elementObj = getElement(self.driver,"xpath","//iframe[contains(@src,'szsj/thirdpage.html')]")
            return elementObj
        except Exception as e:
            raise e

    def getFirstTreesObj(self):
        try:
            elementObj = getElements(self.driver,"xpath","//div[@class='title']")
            return elementObj
        except Exception as e:
            raise e

    def getSecondTreesObj(self):
        try:
            elementObj = getElements(self.driver,"xpath","//a[@class='img_wrap1']")
            return elementObj
        except Exception as e:
            raise e

    def getThirdTreeObj(self):
        try:
            elementObj = getElements(self.driver,"xpath","//div[@class='mini-tree-node']//span[@class='mini-tree-nodetext']")
            return elementObj
        except Exception as e:
            raise e

    def getThirdPageObj(self,pagename):
        # 第三级tab页面标签
        try:
            elementObj = getElement(self.driver,"xpath","//span[contains(text(),pagename)]/parent::td")
            return elementObj
        except Exception as e:
            raise e

    def closeTreeBtnObj(self, treename):
        # 关闭标签
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(), \'"+treename+"\')]/following-sibling::span")
            return elementObj
        except Exception as e:
            raise e