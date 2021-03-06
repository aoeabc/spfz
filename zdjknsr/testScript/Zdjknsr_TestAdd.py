import selenium
from appModules.FrameSwitchAction import FrameSwitchAction
from appModules.LoginAction import LoginAction
from appModules.TreeAction import TreeAction
from appModules.ZdjknsrAddAction import ZdjknsrAddAction
from appModules.ZdjknsrDbAction import ZdjknsrDbAction
from appModules.ZdjknsrXgAction import ZdjknsrXgAction
from appModules.ZdjknsrXgAction import CommonAction
from pageObjects.ZdjknsrFramePage import ZdjknsrFramePage
import time


def test_addZdjknsr():
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgsfengyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库申请")
        # 新增，勾选一个纳税人，提交审批
        pcbh=[]
        #pcbh1=ZdjknsrAddAction.gsycmlAdd(driver,1,"\'蔡永进\'","解除原因","\'稽查定性开企业\'")
        pcbh2 = ZdjknsrAddAction.gsycmlAdd(driver, number=1, spry="蔡永进", reason="解除原因", lx="稽查定性虚开业")
        #pcbh.append(pcbh1)
        pcbh.append(pcbh2)
        return pcbh

    except Exception as e:
        raise e

    finally:
         driver.quit()


def test_dbZdjknsr(pcbh):
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgscaiyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库审批")
        #for p in pcbh:
        ZdjknsrDbAction.gsycmlDb(driver,pcbh=pcbh,spsm='审批说明',spjg="不同意")

    except Exception as e:
        #selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
          driver.quit()


def test_xgZdjknsr(pcbh):
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgsfengyj","888888")
        TreeAction.getFirstTree(driver,"重点监控纳税人库")
        TreeAction.getSecondTree(driver,'重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver,"出库申请")
        # for p in pcbh:
        #     print(p)
        ZdjknsrXgAction.pcXg(driver,pcbh=pcbh,xgsm='修改说明',spry="蔡永进")


    except Exception as e:
        #selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
         driver.quit()

def test():
    try:
        driver=LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver,"szgsfengyj","888888111")
        TreeAction.getFirstTree(driver, "重点监控纳税人库")

    except Exception as e:
        raise e('登录失败，用户名或者密码错误')

if __name__=="__main__":
    #test()
    a = 2
    b = 0
    if not b:
        print("1111")
    else:
        print("22222")




