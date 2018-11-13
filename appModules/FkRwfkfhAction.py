from pageObjects.FkrwfkfhPage import FkrwfkfhPage
from pageObjects.TimePage import TimePage
from pageObjects.FkFramePage import FkFramePage
from appModules.FrameSwitchAction import *
from appModules.CommonAction import *
import time


def rwfkfhAction(driver, rwid, tag):
    try:
        frame = FkFramePage(driver)
        page = FkrwfkfhPage(driver)
        time.sleep(3)
        FrameSwitchAction.frameSwitchTo(driver, frame.rwfkfhPageFrameObj())
        # 选择本机任务，查询结果
        page.rwlxradioObj().click()
        page.queryBtnObj().click()
        time.sleep(3)
        # 查询后，点复核按钮,进入审批页面
        scroll_to(driver, page.fkfhBtnObj(rwid))
        page.fkfhBtnObj(rwid).click()
        # 进入审批页面后，选择结果、反馈复核说明，保存
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.rwfkfhspPageFrameObj())
        time.sleep(3)
        page.fkfhjgObj(tag).click()
        page.fkfhsmObj().send_keys("反馈复核说明")
        page.fkfhbcObj().click()
        time.sleep(2)
        if tag in ['n', 'N', '不同意']:
            page.fkfhMessageBtnObj().click()
            time.sleep(2)
        #  判断是否反馈成功
        message = page.tjMessageObj().get_attribute('innerText')
        assert "成功" in message
        #  分配成功提示信息，点确定
        page.fkfhMessageBtnObj().click()

    except Exception as e:
        raise e