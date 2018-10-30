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