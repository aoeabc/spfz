from pageObjects.FkrwdyPage import FkrwdyPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwdyAction(driver, rwpcbh, hxcl, jsjg, nsrnums=1):
    try:
        page = FkrwdyPage(driver)
        frame1 = FkFramePage(driver)
        #rwpcbh = "任务批次编号5"
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver,frame1.rwdyPageFrameObj())
        page.rwdyBtnObj().click()
        page.queryBtnObj().click()
        page.rwpcmcObj().send_keys(rwpcbh)
        for nsr in range(nsrnums):
            # 后续处理设置
            page.tableclickObj("后续处理", nsr).click()
            time.sleep(2)
            # page.hxclBtnObj().click()
            CommonAction.checkbox(driver, 'mini-218', page.hxclBtnObj())
            time.sleep(2)
            page.hxclSltObj(hxcl).click()
            # 应对机关设置
            page.tableclickObj("接收机关", nsr).click()
            time.sleep(3)
            page.jsjgBtnObj().click()
            CommonAction.putjsjg(driver, jsjg)
            # 选择勾选框
            page.tableclickObj("勾选框", nsr).click()

        page.bcBtnObj().click()
        time.sleep(5)
        # timepage=TimePage(driver)
        # timepage.dateSectBtnObj('rwwcsx_s').click()
        page.rwwcqxBtnObj().click()
        time.sleep(3)
        # 判断是否保存成功
        message=page.tjMessageObj().get_attribute('innerText')
        assert '成功' in message,message
        page.bcMessageBtnObj().click()
        time.sleep(2)
        # 进行发布
        scroll_to(driver, page.rwfbBtnObj(rwpcbh))
        rwid = page.rwfbBtnObj(rwpcbh).get_attribute("href").split("'")[1]
        page.rwfbBtnObj(rwpcbh).click()
        page.zjfbBtnObj().click()
        time.sleep(2)
        # 判断是否发布成功
        message=page.tjMessageObj().get_attribute('innerText')
        assert '成功' in message,message
        page.fbMessageBtnObj().click()
        return rwid

    except Exception as e:
        raise e

