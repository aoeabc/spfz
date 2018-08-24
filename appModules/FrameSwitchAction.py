from pageObjects.TreePage import TreePage
from pageObjects.ZdjknsrFramePage import ZdjknsrFramePage


def frameSwitch(driver):
    frame1 = TreePage(driver)

    driver.switch_to.default_content()
    driver.switch_to.frame(frame1.thirdTreeFrameObj())

class FrameSwitchAction:
    def __init__(self):
        pass

    @staticmethod
    def pcframeSwitch(driver):
        framepage = ZdjknsrFramePage(driver)
        frameSwitch(driver)
        driver.switch_to.frame(framepage.pcPageFrameObj())

    @staticmethod
    def xzframeSwitch(driver):
        framepage = ZdjknsrFramePage(driver)
        frameSwitch(driver)
        driver.switch_to.frame(framepage.xzPageFrameObj())

    @staticmethod
    def dbframeSwitch(driver):
        framepage = ZdjknsrFramePage(driver)
        frameSwitch(driver)
        driver.switch_to.frame(framepage.dbPageFrameObj())

    @staticmethod
    def spframeSwitch(driver):
        framepage = ZdjknsrFramePage(driver)
        frameSwitch(driver)
        driver.switch_to.frame(framepage.spPageFrameObj())