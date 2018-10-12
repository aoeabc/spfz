#coding=utf-8
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.FrameSwitchAction import FrameSwitchAction
from appModules.PageTableAction import PageTableAction
import time


class ZdjknsrDbAction:
    def __init__(self):
        pass

    @staticmethod
    def gsycmlDb(driver, pcbh='', spsm='', spjg=''):
        """ 审批 """
        try:
            tablepage = ZdjknsrTablePage(driver)

            FrameSwitchAction.dbframeSwitch(driver)
            tablepage.spDbsxObj().click()
            time.sleep(2)

            while 1 == 1:
                pcs = ''

                for ele in driver.find_elements_by_xpath("//tr/td[4]"):
                    pcs = pcs+ele.get_attribute('innerText')

                if (pcbh not in pcs) and ('disabled' in tablepage.nextPagerBtn1Obj().get_attribute('class')):
                    print('没找到批次'+pcbh)
                    time.sleep(2)
                    break

                elif  pcbh not in pcs:
                    time.sleep(1)
                    tablepage.nextPagerBtnObj().click()
                    time.sleep(1)

                else:
                    tablepage.dbBtnObj(pcbh).click()
                    FrameSwitchAction.spframeSwitch(driver)
                    PageTableAction.spJg(driver, spsm, spjg)
                    break

        except Exception as e:
            raise e



