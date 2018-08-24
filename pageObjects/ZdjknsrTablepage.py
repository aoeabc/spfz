#coding=utf-8
from util.ObjectMap import *


class ZdjknsrTablePage:
    def __init__(self, driver):
        self.driver = driver

    def addBtnObj(self):
        # 新增解除监控按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@href='javascript:doAdd();']")
            return elementObj
        except Exception as e:
            raise e

    def pcTableObj(self):
        # 批次table
        try:
            elementObj = getElements(self.driver, "xpath", "//table[@id='mini-grid-table-bodydatagrid']//tr[contains(@class,'mini-grid-row')]")
            return elementObj
        except Exception as e:
            raise e

    def pcbhGetObj(self):
        # 获取批次编号
        try:
            elementObj = getElements(self.driver, "xpath","//tr[contains(@class,'mini-grid-row')]/td[2]")
            return elementObj
        except Exception as e:
            raise e

    def nextPagerBtnObj(self):
        #下一页按钮
        try:
            elementObj = getElement(self.driver, "xpath","//div[@id='pager1']//a[@title='下一页']/span")
            return elementObj
        except Exception as e:
            raise e

    def nextPagerBtn1Obj(self):
        #下一页按钮判断
        try:
            elementObj = getElement(self.driver, "xpath","//div[@id='pager1']//a[@title='下一页']")
            return elementObj
        except Exception as e:
            raise e

    def ckpcBtnObj(self, pcbh):
        # 查看批次按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,pcbh) and contains(@onclick,'ck')]")
            return elementObj
        except Exception as e:
            raise e

    def xgpcBtnObj(self, pcbh):
        # 修改批次按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,pcbh) and contains(@onclick,'xg')]")
            return elementObj
        except Exception as e:
            raise e

    def scpcBtnObj(self, pcbh):
        # 删除批次按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,pcbh) and contains(@onclick,'sc')]")
            return elementObj
        except Exception as e:
            raise e

    def lbjlsObj(self):
        # 列表中记录数：每页 20 条, 共 28 条
        try:
            elementObj = getElement(self.driver, "xpath", "//div[@class='mini-pager-right']")
            return elementObj
        except Exception as e:
            raise e

    def checkBoxColumnObj(self):
        # table中纳税人勾选按钮
        try:
            elementObj = getElements(self.driver, "xpath", "//input[@type='checkbox']")
            return elementObj
        except Exception as e:
            raise e

    def jcyySeletedObj(self,number):
        # table中选中监控原因输入框
        try:
            exp="\'mini-7$"+number+"$12\'"
            elementObj = getElement(self.driver, "xpath", "//td[@id="+exp+"]")
            return elementObj
        except Exception as e:
            raise e

    def nsrSeletedObj(self,number):
        # table中选中监控原因输入框
        try:
            exp="\'mini-7$"+number+"\'"
            elementObj = getElement(self.driver, "xpath", "//tr[@id="+exp+"]")
            return elementObj
        except Exception as e:
            raise e

    def jcyyInputObj(self):
        # 监控原因输入框
        try:
            elementObj = getElement(self.driver, "xpath", "//span[@id='mini-38']//input[@class='mini-textbox-input']")
            return elementObj
        except Exception as e:
            raise e

    def tjButtonObj(self):
        # 提交按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[@href='javascript:tj();']/div")
            return elementObj
        except Exception as e:
            raise e

    def nextPsrySBtnObj(self):
        # 选审批人员下拉框按钮
        try:
            #elementObj = getElement(self.driver, "xpath", "//span[@id='nextPsry']//span[@class='mini-buttonedit-icon']")
            elementObj = getElement(self.driver, "css selector", "span#nextPsry>span>span>span>span.mini-buttonedit-icon")

            return elementObj
        except Exception as e:
            raise e

    def nextPsryObj(self,spryname):
        # 选审批人员
        try:
            elementObj = getElement(self.driver, "xpath", "//td[contains(text(),"+spryname+")]")
            return elementObj
        except Exception as e:
            raise e

    def isSeleObj(self):
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@id='mini-36$ck$1']")
            return elementObj
        except Exception as e:
            raise e


    def nextPsryBtnObj(self):
        # 选审批人员提交按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@name='bc']")
            return elementObj
        except Exception as e:
            raise e

    def tjMessageObj(self):
        # 提交审批后的提示信息，用innerText属性获取
        try:
            elementObj = getElement(self.driver, "xpath", "//td[@class='mini-messagebox-content-text']")
            return elementObj
        except Exception as e:
            raise e

    def tjMessageBtnObj(self):
        # 提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def scMessageQdBtnObj(self):
        # 删除批次风险提示信息确定按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'确定')]")
            return elementObj
        except Exception as e:
            raise e

    def scMessageQxBtnObj(self):
        # 删除批次风险提示信息取消按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//span[contains(text(),'取消')]")
            return elementObj
        except Exception as e:
            raise e

    def dbBtnObj(self,pcbh):
        # 审批页面审批按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//a[contains(@onclick,"+pcbh+") and contains(@onclick,'待办')]")
            return elementObj
        except Exception as e:
            raise e

    def spTyBtnObj(self):
        # 审批页面“同意”单选框，属性value（Y/N）可以判断是否选中
        try:
            elementObj = getElement(self.driver, "xpath", "//form/input[@id='ty']")
            return elementObj
        except Exception as e:
            raise e


    def spBtyBtnObj(self):
        # 审批页面“不同意”单选框
        try:
            elementObj = getElement(self.driver, "xpath", "//form/input[@id='bty']")
            return elementObj
        except Exception as e:
            raise e

    def spSmObj(self):
        # 审批页面审批说明
        try:
            elementObj = getElement(self.driver, "xpath", "//textarea[@id='SPSM']")
            return elementObj
        except Exception as e:
            raise e

    def spSaveBtnObj(self):
        # 审批页面保存按钮
        try:
            elementObj = getElement(self.driver, "xpath", "//input[@id='bc']")
            return elementObj
        except Exception as e:
            raise e
