from pageObjects.FkrwfpPage import FkrwfpPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfpAction(driver, rwbh, ydry):
    try:
        frame = FkFramePage(driver)
        page = FkrwfpPage(driver)
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver, frame.rwfpPageFrameObj())
        page.queryBtnObj().click()
        page.rwfpBtnObj(rwbh).click()
        time.sleep(2)
        #  跳转至分配子页面
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.rwfpfpPageFrameObj())
        while 1==1:
            # 应对人员选择
            page.ydryBtnObj().click()
            page.ydrySltBtnObj().click()
            page.ydryqueryObj().send_keys(ydry)
            page.ydryqueryBtnObj().click()
            page.ydryObj(ydry).click()
            time.sleep(3)
            #  勾选框选择
            scroll_to(driver, page.rwfpcheckObj())
            page.rwfpcheckObj().click()
            #  点击确认分配按钮
            time.sleep(2)
            page.qrfqBtnObj().click()
            time.sleep(2)
            #  是否分配提示信息，点确定
            page.rwfpMessageBtnObj().click()
            time.sleep(3)
            #  判断是否分配成功
            message = page.tjMessageObj().get_attribute('innerText')
            assert "成功" in message
            #  分配成功提示信息，点确定
            page.fpMessageBtnObj().click()
            time.sleep(3)

            try:
                #  判断是否还存在未分配的记录，不存在，点确定返回主页面；存在继续执行直到弹出不存在提示。
                if "是否返回" in page.tjMessageObj().get_attribute('innerText'):
                    page.fpfhMessageBtnObj().click()
                    break
            except:
                pass

    except Exception as e:
        raise e