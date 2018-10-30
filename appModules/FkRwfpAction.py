from pageObjects.FkrwfpPage import FkrwfpPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfpAction(driver, rwbh, ydry):
    frame = FkFramePage(driver)
    page = FkrwfpPage(driver)
    time.sleep(3)
    FrameSwitchAction.frameSwitchTo(driver, frame.rwfpPageFrameObj())
    page.queryBtnObj().click()
    page.rwfpBtnObj(rwbh).click()
    time.sleep(2)
    FrameSwitchAction.frameSwitchTo(driver, frame.rwfpfpPageFrameObj())
    page.ydryBtnObj().click()
    page.ydrySltBtnObj().click()
    page.ydryqueryObj().send_keys(ydry)
    page.ydryqueryBtnObj().click()
    page.ydryObj(ydry).click()
    page.qrfqBtnObj().click()