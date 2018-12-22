from pageObjects.FkrwxfPage import FkrwxfPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time

def rwxfAction(driver,rwpcbh):
    try:
        page=FkrwxfPage(driver)
        frame=FkFramePage(driver)
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver, frame.rwxfPageFrameObj())
        page.queryBtnObj().click()
        time.sleep(2)
        page.rwxfSltBtn(rwpcbh).click()
        page.plxfBtn().click()
        time.sleep(2)
        page.plxfMessageBtnObj().click()
        time.sleep(2)
        message = page.tjMessageObj().get_attribute('innerText')
        assert '成功' in message, message
        page.xfMessageBtnObj().click()

    except Exception as e:
        raise e

