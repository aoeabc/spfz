from pageObjects.TreePage import TreePage
import time
class TreeAction:
    def __init__(self):
        print("firsttree.......")

    @staticmethod
    def getFirstTree(driver,firsttreename):
        try:

            tree=TreePage(driver)
            time.sleep(3)
            driver.switch_to.frame(tree.mainTreeFrameObj())
            trees=tree.getFirstTreesObj()
            for tre in trees:
                if firsttreename in tre.get_attribute("innerText").replace('\r\n',''):
                    tre.click()
        except Exception as e:
            print(e)

    @staticmethod
    def getSecondTree(driver,secondtreename):
        try:
            tree=TreePage(driver)
            trees=tree.getSecondTreesObj()
            for tre in trees:
                if secondtreename in tre.get_attribute("innerText").replace('\r\n',''):
                    tre.click()

        except Exception as e:
            raise e

    @staticmethod
    def getThirdTree(driver,thirdtreename):
        try:
            tree=TreePage(driver)
            driver.switch_to.default_content()
            driver.switch_to.frame(tree.thirdTreeFrameObj())
            trees=tree.getThirdTreeObj()
            for tre in trees:
                if thirdtreename==tre.get_attribute("innerText"):
                    tre.click()

        except Exception as e:
            raise e