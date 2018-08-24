#coding=utf-8
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.FrameSwitchAction import FrameSwitchAction
from appModules.PageTableAction import PageTableAction


class ZdjknsrDbAction:
    def __init__(self):
        pass


    @staticmethod
    def gsycmlDb(driver,pcbh,spsm,spjg):
        try:
            tablepage=ZdjknsrTablePage(driver)

            FrameSwitchAction.dbframeSwitch(driver)
            tablepage.dbBtnObj(pcbh).click()
            FrameSwitchAction.spframeSwitch(driver)
            PageTableAction.spJg(driver,spsm,spjg)


        except Exception as e:
            raise e



