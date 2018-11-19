from pageObjects.FkrwfktzPage import FkrwfktzPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfktzAction(driver, narid = None):
    try:
        frame = FkFramePage(driver)
        page = FkrwfktzPage(driver)
        time.sleep(3)
        # 任务反馈页面，点击查询、应对反馈
        FrameSwitchAction.frameSwitchTo(driver, frame.ydjgtzPageFrameObj())
        page.queryBtnObj().click()
        time.sleep(2)
        # 点击调整
        if narid == None:
            ele = page.ydjgtzBtnObj()
            # rwid = ele.get_attribute('onclick').split("'")[1]
            ele.click()
        else:
            page.ydjgtzBtnObj(narid).click()
        time.sleep(2)
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.ydjgtztzPageFrameObj())
        narid=page.nsrsbhObj().get_attribute('innerText').split('（')[1].split("）")[0]
        page.sfjbphObj('y').click()
        page.fplgCheckboxObj().click()
        page.pzhdCheckboxObj().click()
        scroll_to(driver, page.ydgzqksmObj())
        page.nsrsfywtObj("n").click()
        page.ydgzqksmObj().send_keys("应对情况说明")
        page.rwtjBtnObj().click()
        time.sleep(2)
        page.rwfktjMessageBtnObj().click()
        time.sleep(2)
        #  判断是否反馈成功
        message = page.tjMessageObj().get_attribute('innerText')
        assert "成功" in message
        #  分配成功提示信息，点确定
        page.fkMessageBtnObj().click()
        return narid

    except Exception as e:
        raise e
