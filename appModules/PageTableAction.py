#coding=utf-8
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.CommonAction import CommonAction
import time

class PageTableAction:
    def __init__(self):
        pass


    @staticmethod
    def tjPsry(driver,spry):
        try:

            tablepage=ZdjknsrTablePage(driver)

            tablepage.tjButtonObj().click()
            time.sleep(5)
            CommonAction.checkbox(driver,'nextPsry',tablepage.nextPsrySBtnObj())
            tablepage.nextPsryObj(spry).click()
            tablepage.nextPsryBtnObj().click()
            time.sleep(2)
            print(tablepage.tjMessageObj().get_attribute('innerText'))
            tablepage.tjMessageBtnObj().click()
            time.sleep(3)

        except Exception as e:
            print(e)


    @staticmethod
    def nsrSelector(driver,number,reason):
        try:
            tablepage=ZdjknsrTablePage(driver)
            for num in range(0,number):
                nsrxx=tablepage.nsrSeletedObj(str(num)).get_attribute('innerText')
                print("当前选中的纳税人信息有：")
                print(nsrxx)
                tablepage.jcyySeletedObj(str(num)).click()
                tablepage.jcyyInputObj().send_keys(reason)


        except Exception as e:
            raise e

    @staticmethod
    def getPcbh(driver):
        try:
            pcbh=[]
            tablepage = ZdjknsrTablePage(driver)
            time.sleep(3)

            while (1==1) :
                for obj in tablepage.pcbhGetObj():
                    pcbh.append(obj.text)

                if 'disabled' in tablepage.nextPagerBtn1Obj().get_attribute('class'):
                    break
                time.sleep(1)
                tablepage.nextPagerBtnObj().click()
                time.sleep(1)

            return pcbh

        except Exception as e:

            raise e


    @staticmethod
    def spJg(driver,spsm,spjg):
        try:
            tablepage = ZdjknsrTablePage(driver)

            if spjg == '同意':
                tablepage.spTyBtnObj().click()
            else:
                tablepage.spBtyBtnObj().click()
            tablepage.spSmObj().send_keys(spsm)
            tablepage.spSaveBtnObj().click()
            print(tablepage.tjMessageObj().get_attribute('innerText'))
            tablepage.tjMessageBtnObj().click()




        except Exception as e:

            raise e

