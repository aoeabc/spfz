from appModules.FkRwdyAction import *
from appModules.FkRwxfAction import *
from appModules.FkRwfpAction import *
from appModules.FkRwfkAction import *
from appModules.FkRwfkfhAction import *
from appModules.FkRwfktzAction import *
from appModules.FkRwfktzspAction import *
from appModules.LoginTree import LoginTree
from appModules.TreeAction import TreeAction

def test():
    try:
        url = 'http://86.100.16.15:8001'
        driver = LoginTree.logintree(url,'fxfx_sjcs','sy123','风险管理系统','风险应对','应对结果调整')
        # rwdyAction(driver, "任务批次编号8", "应对处置", "14403000000")
        # # 任务批次编号，后续处理（任务统筹、应对处置），接收机关
        # TreeAction.getThirdTree(driver,'任务下发')
        # rwxfAction(driver, "任务批次编号8")
        # TreeAction.getThirdTree(driver, '任务分配')
        # rwfpAction(driver, "任务批次编号6", "市局用户")
        # TreeAction.getThirdTree(driver, '任务反馈')
        #　rwfkAction(driver, "测试1005")
        # TreeAction.getThirdTree(driver, '反馈结果复核')
        # rwfkfhAction(driver, '6e6c9c27ea904066a9bb3b158b854972', "不同意")
        # TreeAction.getThirdTree(driver, '应对结果调整')
        # nsrid = rwfktzAction(driver)  #  返回任务id
        # TreeAction.getThirdTree(driver, '应对结果调整审批')
        # rwfktzspAction(driver, nsrid)


    except Exception as e:
        raise e


test()
