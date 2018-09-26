import xlrd,xlwt
from xlutils.copy import copy
from appModules.LoginAction import LoginAction
from appModules.TreeAction import TreeAction
from appModules.ZdjknsrAddAction import ZdjknsrAddAction
from appModules.ZdjknsrDbAction import ZdjknsrDbAction
from appModules.ZdjknsrXgAction import ZdjknsrXgAction

import time

global able_sp,able_xg,able_zs

able_sp={}
able_xg={}
able_zs={}


def test_addZdjknsr(row):
    try:
        driver = LoginAction.driver(row[2])
        LoginAction.login(driver, row[3].split(";")[0], row[3].split(";")[1])
        TreeAction.getFirstTree(driver, row[4])
        TreeAction.getSecondTree(driver, row[5])
        TreeAction.getThirdTree(driver, row[6])
        pas = row[7].split(";")
        global able_sp
        for pa in pas:
            p=eval(pa)
            pcbh = ZdjknsrAddAction.gsycmlAdd(driver, number=int(p.get('number')), spry=p.get('spry'), reason=p.get('reason'), lx=p.get('lx'))

            able_sp[pcbh]=p.get('lx')
        flag='Pass'
        row[9]=flag
        row[10]=able_sp

        return row


    except Exception as e:
        raise e

    finally:
        driver.quit()


def test_dbZdjknsr(row):
    try:
        driver = LoginAction.driver(row[2])
        LoginAction.login(driver, row[3].split(";")[0], row[3].split(";")[1])
        TreeAction.getFirstTree(driver, row[4])
        TreeAction.getSecondTree(driver, row[5])
        TreeAction.getThirdTree(driver, row[6])
        pas=row[7].split(';')
        global able_xg, able_sp, able_zs
        for pa in pas:
            p=eval(pa)
            pcbh=list(able_sp.keys())[0]
            print(pcbh)
            pcbhs=[]
            ZdjknsrDbAction.gsycmlDb(driver, pcbh=pcbh, spsm=p.get('spsm'), spjg=p.get('spjg'))
            if p.get('spjg')=='不同意':
                able_xg[pcbh]=able_sp.pop(pcbh)
            elif p.get('spjg')=='同意' and able_sp[pcbh] == '稽查定性虚开企业':
                able_zs[pcbh] = able_sp.pop(pcbh)
            else:
                del able_sp[pcbh]
            pcbhs.append(pcbh)
        flag = 'Pass'
        row[9]=flag
        row[10]=pcbhs

        return row


    except Exception as e:
        # selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
        driver.quit()


def test_xgZdjknsr(pcbh):
    try:
        driver = LoginAction.driver("http://86.100.16.15:8001")
        LoginAction.login(driver, "szgscaiyj", "888888")
        TreeAction.getFirstTree(driver, "重点监控纳税人库")
        TreeAction.getSecondTree(driver, '重点监控纳税人手动出库')
        TreeAction.getThirdTree(driver, "出库审批")
        for p in pcbh:
            print(p)
            ZdjknsrXgAction.pcXg(driver, pcbh=p, xgsm='审批说明', spry="蔡永进")


    except Exception as e:
        # selenium.common.exceptions.UnexpectedAlertPresentException: Alert Text: 停止运行此脚本吗?
        raise e

    finally:
        driver.quit()

def readXl():
    workbook = xlrd.open_workbook(r'd:\test_data.xls',formatting_info=True)
    sheetname = workbook.sheet_by_index(0)
    rows = sheetname.nrows
    f = copy(workbook)
    sheet1 = f.get_sheet(0)
    print(rows)
    for row in range(rows):
        if sheetname.row_values(row)[1] == 'test_addZdjknsr' and sheetname.row_values(row)[8] == 'Y':
            data = test_addZdjknsr(sheetname.row_values(row))
            sheet1.write(row, 9, data[9],set_style())
            sheet1.write(row, 10, list(data[10].keys()), set_style())

        elif sheetname.row_values(row)[1] == 'test_dbZdjknsr' and sheetname.row_values(row)[8] == 'Y':
            data = test_dbZdjknsr(sheetname.row_values(row))
            sheet1.write(row, 9, data[9],set_style())
            sheet1.write(row, 10, data[10], set_style())

        elif sheetname.row_values(row)[1] == 'test_xgZdjknsr' and sheetname.row_values(row)[8] == 'Y':
            data = test_xgZdjknsr(sheetname.row_values(row))
            sheet1.write(row, 9, data[9],set_style())

    f.save(r'd:\test_data1.xls')

def set_style():
    #   设置颜色
    pattern = xlwt.Pattern()
    pattern.pattern = xlwt.Pattern.SOLID_PATTERN
    pattern.pattern_fore_colour = 17
    #   设置边框
    borders = xlwt.Borders()
    borders.bottom=xlwt.Borders.THIN
    borders.left=xlwt.Borders.THIN
    borders.right=xlwt.Borders.THIN
    borders.top=xlwt.Borders.THIN
    borders.bottom_colour=0x40
    borders.left_colour=0x40
    borders.right_colour=0x40
    borders.top_colour=0x40


    style = xlwt.XFStyle()
    style.pattern = pattern
    style.borders = borders

    return style
if __name__ == "__main__":
    readXl()
