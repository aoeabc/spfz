#coding=utf-8
from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.FrameSwitchAction import FrameSwitchAction
from appModules.PageTableAction import PageTableAction
from appModules.CommonAction import CommonAction

class ZdjknsrAddAction:
    def __init__(self):
        pass


    @staticmethod
    def gsycmlAdd(driver,number,spry,reason,lx):
        try:
            querypage=ZdjknsrQueryPage(driver)
            tablepage=ZdjknsrTablePage(driver)

            FrameSwitchAction.pcframeSwitch(driver)

            CommonAction.checkbox(driver, "jklx", querypage.jklxObj())
            if not querypage.jklxCbObj().is_selected():

                querypage.jklxCbObj().click()
            querypage.queryBtnObj().click()

            b1=PageTableAction.getPcbh(driver)

            tablepage.addBtnObj().click()

            FrameSwitchAction.xzframeSwitch(driver)

            if '稽查定性虚开企业' in lx:
                CommonAction.checkbox(driver, "jklx", querypage.jklxObj())
                querypage.xzjklxCbObj(lx).click()


            querypage.queryBtnObj().click()

            PageTableAction.nsrSelector(driver,number,reason)

            PageTableAction.tjPsry(driver,spry)

            FrameSwitchAction.pcframeSwitch(driver)

            b2 = PageTableAction.getPcbh(driver)

            for num1 in b2:
                if num1 not in b1:
                    newpc=num1

            return newpc

        except Exception as e:
            raise e



