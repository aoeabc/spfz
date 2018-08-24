from util.ObjectMap import *

class ZdjknsrFramePage:
    def __init__(self, driver):
        self.driver = driver

    def pcPageFrameObj(self):
        # 批次tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'zdnsrk/zdnsrk_pc.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def xzPageFrameObj(self):
        # 新增tab页
        try:
            elementObj=getElement(self.driver,"xpath","//iframe[contains(@src,'zdnsrk/jczdnsr_xz.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def xgPageFrameObj(self):
        # 修改tab页
        try:
            elementObj=getElement(self.driver,"xpath","//iframe[contains(@src,'jczdnsr_xg.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def dbPageFrameObj(self):
        # 代办页面
        try:
            elementObj=getElement(self.driver,"xpath","//iframe[contains(@src,'zdnsrk_rwdb.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def spPageFrameObj(self):
        # 审批页面
        try:
            elementObj=getElement(self.driver,"xpath","//iframe[contains(@src,'zdnsrk_sp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e