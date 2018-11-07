from pageObjects.FkrwfkPage import FkrwfkPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfkAction(driver, rwbh):
    try:
        frame = FkFramePage(driver)
        page = FkrwfkPage(driver)
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver, frame.rwfkPageFrameObj())
        page.queryBtnObj().click()
        time.sleep(2)
        page.rwfkBtnObj(driver, rwbh).click()
        time.sleep(2)
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.rwfkfkPageFrameObj())
        


    except Exception as e:
        raise e
