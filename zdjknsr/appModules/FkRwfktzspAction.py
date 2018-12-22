from pageObjects.FkrwfktzspPage import FkrwfktzspPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfktzspAction(driver,nsrid=None, tag = None):
    try:
        frame = FkFramePage(driver)
        page = FkrwfktzspPage(driver)
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver, frame.ydjgtzspPageFrameObj())
        page.queryBtnObj().click()
        time.sleep(3)
        # 点审批按钮
        page.tzspBtnObj(nsrid).click()
        # 切换到审批页面
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.ydjgtzspspPageFrameObj())
        # 选择审批结果、审批说明
        page.tzspjgObj().click()
        page.spyjsmObj().send_keys("反馈复核说明")
        page.spbcObj().click()
        time.sleep(2)
        if tag !=None:
            page.tjspMessageBtnObj().click()
            time.sleep(2)
        #  判断是否反馈成功
        message = page.tjMessageObj().get_attribute('innerText')
        assert "成功" in message
        #  分配成功提示信息，点确定
        page.tjspMessageBtnObj().click()


    except Exception as e:
        raise e