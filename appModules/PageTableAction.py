#coding=utf-8
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
from appModules.CommonAction import CommonAction
import time


class PageTableAction:
    def __init__(self):
        pass

    @staticmethod
    def tjPsry(driver, spry):
        # 提交审批功能
        try:

            tablepage = ZdjknsrTablePage(driver)

            tablepage.tjButtonObj().click()
            CommonAction.putPsry(driver,spry,"nextPsry")

        except Exception as e:
            raise e

    @staticmethod
    def nsrSelector(driver,number,reason):
        # 重点监控纳税人新增时，选择纳税人
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
        # 遍历批次编号
        try:
            pcbh = []
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
        # 审批时，审批结果处理
        # 审批结果，选同意或者不同意；
        try:
            tablepage = ZdjknsrTablePage(driver)
            tablepage.spSmObj().send_keys(spsm)
            time.sleep(2)
            if spjg == '同意':
                while not tablepage.spTyBtnObj().is_selected():
                    tablepage.spTyBtnObj().click()
                tablepage.spSmObj().send_keys(spsm)

                if tablepage.spLxObj().get_attribute('value') == '工商异常名录':
                    tablepage.spSaveBtnObj().click()
                    print(tablepage.tjMessageObj().get_attribute('innerText'))
                    tablepage.tjMessageBtnObj().click()

                else:
                    tablepage.spTjBtnObj().click()
                    CommonAction.putPsry(driver, "蔡永进", "nextZsry")

            elif spjg == '不同意':
                while not tablepage.spBtyBtnObj().is_selected():
                    tablepage.spBtyBtnObj().click()

                tablepage.spSmObj().send_keys(spsm)

                if tablepage.spLxObj().get_attribute('value') == '工商异常名录':
                    tablepage.spSaveBtnObj().click()
                    time.sleep(2)
                    message=tablepage.tjMessageObj().get_attribute('innerText')
                    assert '成功' in message, "保存失败"
                    tablepage.tjMessageBtnObj().click()

                else:
                    tablepage.spTjBtnObj().click()
                    time.sleep(2)
                    message = tablepage.tjMessageObj().get_attribute('innerText')
                    assert '成功' in message,"保存失败"
                    tablepage.tjMessageBtnObj().click()

        except Exception as e:

            raise e

    @staticmethod
    def pcXg(driver,xgsm):
        # 批次修改,修改说明只能改解除原因
        try:
            tablepage = ZdjknsrTablePage(driver)
            for ele in tablepage.jcyyXgSeletedObj():
                ele.click()
                tablepage.jcyyXgInputObj().send_keys(xgsm)

        except Exception as e:
            raise e
