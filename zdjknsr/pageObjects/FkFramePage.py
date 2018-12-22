from util.ObjectMap import *


class FkFramePage:
    def __init__(self, driver):
        self.driver = driver

    def jsjgtreeFrameObj(self):
        # 任务定义页,弹出的选择税务机关窗口
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydgl_rwdy_swjg_tree.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwdyPageFrameObj(self):
        # 任务定义tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydgl_rwdy.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwxfPageFrameObj(self):
        # 任务下发tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydgl_rwxf.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfpPageFrameObj(self):
        # 任务分配主tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfpfpPageFrameObj(self):
        # 任务分配分配tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfp_fp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfkPageFrameObj(self):
        # 任务反馈tab页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfk.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfkfkPageFrameObj(self):
        # 应对反馈tab页，任务反馈-》应对反馈
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfk_fk.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfkfkfkPageFrameObj(self):
        # 应对反馈tab页，任务反馈-》应对反馈
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfk_sjyh_sk.webfaste')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfkfhPageFrameObj(self):
        # 应对反馈复核批次页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_fkjgsp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def rwfkfhspPageFrameObj(self):
        # 应对反馈复核详情页
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_fkjgsp_sp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtzPageFrameObj(self):
        # 应对结果调整批次页面
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_ydjg_tz.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtztzPageFrameObj(self):
        # 应对结果调整详情页面
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_rwfk_sjyh_sk.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtzspPageFrameObj(self):
        # 应对结果调整审批批次页面
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_ydjg_tzsp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e

    def ydjgtzspspPageFrameObj(self):
        # 应对结果调整审批详情页面
        try:
            elementObj = getElement(self.driver, "xpath", "//iframe[contains(@src,'ydcz_ydjg_tzsp_sp.webfaster')]")
            return elementObj
        except Exception as e:
            raise e