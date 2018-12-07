from conf.VarConfig import *
from conf.ParserExcel import ParserExcel
from appModules.ZdjknsrAddAction import ZdjknsrAddAction
from appModules.ZdjknsrDbAction import ZdjknsrDbAction
from appModules.ZdjknsrXgAction import ZdjknsrXgAction
from appModules.LoginTree import LoginTree

def test_addZdjknsr(url, username, password, ftree, stree, ttree=None):
    try:

        driver=LoginTree.driver(url, username, password, ftree, stree, ttree=None)
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
        driver=LoginTree.driver("http://86.100.16.15:8001")
        LoginTree.login(driver,"szgscaiyj","888888")
        LoginTree.getFirstTree(driver,"重点监控纳税人库")
        LoginTree.getSecondTree(driver,'重点监控纳税人手动出库')
        LoginTree.getThirdTree(driver,"出库审批")
        #for p in pcbh:
        ZdjknsrDbAction.gsycmlDb(driver,pcbh=pcbh,spsm='审批说明',spjg="不同意")

    except Exception as e:
        #selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
          driver.quit()


def test_xgZdjknsr(pcbh):
    try:
        driver=LoginTree.driver("http://86.100.16.15:8001")
        LoginTree.login(driver,"szgsfengyj","888888")
        LoginTree.getFirstTree(driver,"重点监控纳税人库")
        LoginTree.getSecondTree(driver,'重点监控纳税人手动出库')
        LoginTree.getThirdTree(driver,"出库申请")
        # for p in pcbh:
        #     print(p)
        ZdjknsrXgAction.pcXg(driver,pcbh=pcbh,xgsm='修改说明',spry="蔡永进")


    except Exception as e:
        #selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
         driver.quit()

def run_main():
    excel = ParserExcel()
    excel.loadWorkBook(zdjkdateFilePath)
    sheet = excel.getSheetByName("测试脚本")
    datacols = excel.getRowsNumber(sheet)
    for i in range(datacols):
        row = excel.getRow(sheet, i)
        func = row[zdjk_funcname].value
        is_run = row[zdjk_is_run-1].value
        url = row[zdjk_url].value
        username = row[zdjk_username_pwd].value.split(";")[0]
        password = row[zdjk_username_pwd].value.split(";")[-1]
        ftree = row[zdjk_firsttree].value
        stree = row[zdjk_secondtree].value
        ttree = row[zdjk_thirdtree].value

        if func == "新增" and is_run == "Y" :
            try:
                result = test_addZdjknsr(row)
                excel.writeCell(sheet, result, rowNo=i, colsNo=zdjk_result_parameter)
                excel.writeCell(sheet, "Pass", rowNo=i, colsNo=zdjk_result)
            except Exception as e:
                raise e





if __name__ == "__main__":
    run_main()