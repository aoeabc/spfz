from appModules.FkRwdyAction import *
from appModules.FkRwxfAction import *
from appModules.FkRwfpAction import *
from appModules.LoginTree import LoginTree
from appModules.TreeAction import TreeAction

def test():
    try:
        url = 'http://86.100.16.15:8001'
        # driver = LoginTree.logintree(url,'fxfx_sjcs','sy123','风险管理系统','风险应对','任务定义')
        # rwdyAction(driver, "任务批次编号8", "应对处置", "14403000000")
        # # 任务批次编号，后续处理（任务统筹、应对处置），接收机关
        # TreeAction.getThirdTree(driver,'任务下发')
        # rwxfAction(driver, "任务批次编号8")
        # TreeAction.getThirdTree(driver, '任务分配')
        driver = LoginTree.logintree(url, 'fxfx_sjcs', 'sy123', '风险管理系统', '风险应对', '任务分配')
        rwfpAction(driver, "任务批次编号6", "市局用户")

    except Exception as e:
        raise e


test()
