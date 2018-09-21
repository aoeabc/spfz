#coding=utf-8
from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.FrameSwitchAction import FrameSwitchAction
from appModules.PageTableAction import PageTableAction
from appModules.CommonAction import CommonAction
import time

class ZdjknsrXgAction:

    @staticmethod
    def pcXg(driver,xgsm='',spry='',pcbh=''):
        try:
            querypage=ZdjknsrQueryPage(driver)
            tablepage=ZdjknsrTablePage(driver)


            FrameSwitchAction.pcframeSwitch(driver)

            CommonAction.checkbox(driver, "jklx", querypage.jklxObj())
            if not querypage.jklxCbObj().is_selected():

                querypage.jklxCbObj().click()
            querypage.queryBtnObj().click()
            time.sleep(2)

            while 1==1:
                pcs=''

                for ele in driver.find_elements_by_xpath("//tr/td[7]/a"):
                    pcs=pcs+ele.get_attribute('onclick')


                if (pcbh not in pcs) and ('disabled' in tablepage.nextPagerBtn1Obj().get_attribute('class')):
                    print('没找到批次'+pcbh)
                    time.sleep(2)
                    break


                elif  pcbh not in pcs:
                    time.sleep(1)
                    tablepage.nextPagerBtnObj().click()
                    time.sleep(1)


                else:
                    tablepage.xgpcBtnObj(pcbh).click()
                    FrameSwitchAction.xgframeSwitch(driver)
                    PageTableAction.pcXg(driver,xgsm)
                    PageTableAction.tjPsry(driver,spry)

                    break

        except Exception as e:
            raise e

