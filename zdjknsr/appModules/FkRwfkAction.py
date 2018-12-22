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
        # 任务反馈页面，点击查询、应对反馈
        FrameSwitchAction.frameSwitchTo(driver, frame.rwfkPageFrameObj())
        page.queryBtnObj().click()
        time.sleep(2)
        page.rwfkBtnObj(rwbh).click()
        time.sleep(2)
        # 应对反馈页面，点击开始反馈
        driver.switch_to.default_content()
        frameSwitch(driver)
        driver.switch_to.frame(frame.rwfkfkPageFrameObj())
        rwid=[]
        while True:
            try:
                ele = page.ksfkBtnObj()
            except Exception:
                break
            rwid.append(ele.get_attribute("href").split("'")[1])
            print(rwid)
            time.sleep(5)
            print("延时5s,准备点击开始反馈按钮")
            print(ele)
            #
            ele.click()
            # 反馈页面，进行反馈
            driver.switch_to.default_content()
            frameSwitch(driver)
            driver.switch_to.frame(frame.rwfkfkfkPageFrameObj())
            print("当前页面为："+driver.current_url)
            page.sfsjssObj("n").click()
            page.sfwflxObj("n").click()
            page.sfjbphObj("y").click()
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
            time.sleep(5)
            print("延时10s,准备切换到fkfk页面")
            driver.switch_to.default_content()
            frameSwitch(driver)
            driver.switch_to.frame(frame.rwfkfkPageFrameObj())
            print("当次反馈完成，切换到fkfk页面")
            print("当前页面为：" + driver.current_url)
            try:
                while "Loading" in page.tjMessageObj().get_attribute('innerText'):
                    time.sleep(1)
                    print("请稍后······")
            except:
                print("加载完成")
                pass

        return rwid

    except Exception as e:
        raise e
