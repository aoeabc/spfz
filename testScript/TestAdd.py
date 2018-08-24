from selenium import webdriver
from appModules.LoginAction import LoginAction
from appModules.TreeAction import TreeAction
from appModules.ZdjknsrAddAction import ZdjknsrAddAction
from appModules.ZdjknsrDBAction import ZdjknsrDbAction
from appModules.QueryPageAction import QueryPageAction

import time

def test_addZdjknsrGS():
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgsfengyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库申请")
        # 新增工商异常名录，勾选一个纳税人，提交审批
        pcbh=ZdjknsrAddAction.gsycmlAdd(driver,1,"\'蔡永进\'","解除原因")
        print("新增的批次为:"+pcbh)
        return pcbh


    except Exception as e:
        raise e

    finally:
         driver.quit()

def test_dbZdjknsrGS(pcbh):
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgscaiyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库审批")
        print("审批的批次为："+pcbh)
        ZdjknsrDbAction.gsycmlDb(driver,pcbh,'审批说明',"同意")


    except Exception as e:
        raise e

    finally:
         driver.quit()

def test_addZdjknsrJc():
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgsfengyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库申请")
        # 新增工商异常名录，勾选一个纳税人，提交审批
        QueryPageAction.doQuery(driver)


    except Exception as e:
        raise e

    finally:
         driver.quit()

        
if __name__=="__main__":
    pcbh=test_addZdjknsrGS()
    #test_dbZdjknsrGS(pcbh)
    #test_addZdjknsrJc()
