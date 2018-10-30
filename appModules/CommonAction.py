from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from selenium.webdriver.common.keys import Keys
from appModules.FrameSwitchAction import *
from pageObjects.FkFramePage import FkFramePage
from pageObjects.FkrwdyPage import FkrwdyPage
from pageObjects.TimePage import TimePage
import time


class CommonAction:

    @staticmethod
    def checkbox(driver, eleid, element):
        # eleid：为下拉框的ID
        # element：下拉框的按钮节点，类型为对象
        # 点击下拉框按钮，直到下拉框弹出来。
        try:

            querytable = ZdjknsrQueryPage(driver)

            while 'mini-buttonedit-popup' not in querytable.checkboxObj(eleid).get_attribute("class"):

                element.click()
                if 'mini-buttonedit-popup' in querytable.checkboxObj(eleid).get_attribute("class"):
                    break
        except Exception as e:
            raise e

    @staticmethod
    def putPsry(driver, spry, id):
        #  提交审批指定人；
        # id:下拉框ID
        # spry:审批人员名称，例如："蔡永进"
        try:

            tablepage = ZdjknsrTablePage(driver)
            time.sleep(5)
            CommonAction.checkbox(driver, id, tablepage.nextPsrySBtnObj(id))
            tablepage.nextPsryObj(spry).click()
            tablepage.nextPsryBtnObj().click()
            time.sleep(2)
            message = tablepage.tjMessageObj().get_attribute('innerText')
            assert '成功' in message,'保存失败'
            tablepage.tjMessageBtnObj().click()
            time.sleep(3)

        except Exception as e:
            raise e

    @staticmethod
    def settime(driver, frameaction, id, year, month, date):
        # 时间控件设置时间：CommonAction.settime(driver,frame.pcPageFrameObj(),'tjsjq','2017','2','22')
        # id ：时间控件ID
        # frameaction 当前页面的框架
        # 时间小于10 ，只输入一位
        try:
            FrameSwitchAction.frameSwitchTo(driver, frameaction)
            setyear(driver, id, year)
            FrameSwitchAction.frameSwitchTo(driver, frameaction)
            setmonth(driver, id, month)
            FrameSwitchAction.frameSwitchTo(driver, frameaction)
            setdate(driver, id, year, month, date)
            FrameSwitchAction.frameSwitchTo(driver, frameaction)

        except Exception as e:
            raise e

    @staticmethod
    def putjsjg(driver,ydjg):

        try:
            page=FkrwdyPage(driver)
            frame=FkFramePage(driver)
            driver.switch_to.default_content()
            driver.switch_to.frame(frame.jsjgtreeFrameObj())
            page.ydjgSltObj(ydjg).click()
            time.sleep(1)
            page.ydjgtreeBtnObj().click()
            time.sleep(2)
            driver.switch_to.default_content()
            frameSwitch(driver)
            driver.switch_to.frame(frame.rwdyPageFrameObj())
            #FrameSwitchAction.frameSwitchTo(driver, frame.rwdyPageFrameObj())

        except Exception as e:
            raise e


def setyear(driver, id, year):
    try:
        query = TimePage(driver)
        query.dateSectBtnObj(id).click()  # tisjq
        driver.switch_to.default_content()
        driver.switch_to.frame(query.dateFrameObj())
        query.timeYearObj().click()
        query.timeYearObj().send_keys(int(year))
        query.timeMonthObj().send_keys(Keys.ENTER)

    except Exception as e:
        raise e


def setmonth(driver, id, month):
    try:
        query = TimePage(driver)
        query.dateSectBtnObj(id).click()  # tisjq
        driver.switch_to.default_content()
        driver.switch_to.frame(query.dateFrameObj())
        query.timeMonthObj().click()
        query.timeMonthObj().send_keys(int(month))
        query.timeMonthObj().send_keys(Keys.ENTER)

    except Exception as e:
        raise e

def setdate(driver, id, year, month, date):
    try:
        query = TimePage(driver)
        query.dateSectBtnObj(id).click()  # tisjq
        driver.switch_to.default_content()
        driver.switch_to.frame(query.dateFrameObj())
        query.timeDateObj(year, month, date).click()
        query.dateOKBtnObj().click()

    except Exception as e:
        raise e

def scroll_to(driver,ele):
    driver.execute_script("arguments[0].scrollIntoView();", ele)