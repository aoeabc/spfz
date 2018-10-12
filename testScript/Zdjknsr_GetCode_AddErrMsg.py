import xlrd
import xlwt
from xlutils.copy import copy
from appModules.ZdjknsrAddAction import ZdjknsrAddAction
from appModules.ZdjknsrDbAction import ZdjknsrDbAction
from appModules.ZdjknsrXgAction import ZdjknsrXgAction
from appModules.LoginTree import LoginTree
from appModules.SetStyle import set_style

import time

global able_sp, able_xg, able_zs

able_sp = {}
able_xg = {}
able_zs = {}


def test_addZdjknsr(row):
    try:
        driver = LoginTree.logintree(row[2], row[3].split(";")[0], row[3].split(";")[1], row[4], row[5], row[6])
        pas = row[7].split(";")
        global able_sp
        for pa in pas:
            p = eval(pa)
            pcbhs = []
            pcbh = ZdjknsrAddAction.gsycmlAdd(driver, number=int(p.get('number')), spry=p.get('spry'),
                                              reason=p.get('reason'), lx=p.get('lx'))

            able_sp[pcbh] = p.get('lx')
            pcbhs.append(pcbh)
        flag = 'Pass'
        row[9] = flag
        row[10] = pcbhs
        return row

    except Exception as e:
        raise e

    finally:
        driver.quit()


def test_dbZdjknsr(row):
    try:
        driver = LoginTree.logintree(row[2], row[3].split(";")[0], row[3].split(";")[1], row[4], row[5], row[6])
        pas = row[7].split(';')
        global able_xg, able_sp, able_zs
        for pa in pas:
            p = eval(pa)
            pcbh = list(able_sp.keys())[0]
            print(pcbh)
            pcbhs = []
            ZdjknsrDbAction.gsycmlDb(driver, pcbh=pcbh, spsm=p.get('spsm'), spjg=p.get('spjg'))
            if p.get('spjg') == '不同意':
                able_xg[pcbh] = able_sp.pop(pcbh)
            elif p.get('spjg') == '同意' and able_sp[pcbh] == '稽查定性虚开企业':
                able_zs[pcbh] = able_sp.pop(pcbh)
            else:
                del able_sp[pcbh]
            pcbhs.append(pcbh)
        flag = 'Pass'
        row[9] = flag
        row[10] = pcbhs

        return row

    except Exception as e:
        raise e

    finally:
        driver.quit()


def test_xgZdjknsr(row):
    try:
        driver = LoginTree.logintree(row[2], row[3].split(";")[0], row[3].split(";")[1], row[4], row[5], row[6])
        pas = row[7].split(';')
        global able_xg, able_sp, able_zs
        for pa in pas:
            p = eval(pa)
            pcbh=list(able_xg.keys())[0]
            pcbhs=[]
            ZdjknsrXgAction.pcXg(driver, pcbh=pcbh, xgsm=p.get('xgsm'), spry=p.get('spry'))
            able_sp[pcbh] = able_xg.pop(pcbh)
            pcbhs.append(pcbh)

        flag = 'Pass'
        row[9] = flag
        row[10] = pcbhs

        return row
    except Exception as e:
        raise e

    finally:
        driver.quit()

def readXl():
    workbook = xlrd.open_workbook(r'd:\Lww\py\zdjknsr\conf\test_data.xls', formatting_info=True)
    sheetname = workbook.sheet_by_index(0)
    rows = sheetname.nrows
    f = copy(workbook)
    sheet1 = f.get_sheet(0)
    print(rows)
    for row in range(rows):

        if sheetname.row_values(row)[1] == '新增' and sheetname.row_values(row)[8] == 'Y':
            try:

                data = test_addZdjknsr(sheetname.row_values(row))
            except Exception as e:

                sheet1.write(row, 9, 'Fail', set_style())
                sheet1.write(row, 10, str(e), set_style())
                continue
            else:
                sheet1.write(row, 9, data[9], set_style())
                sheet1.write(row, 10, data[10], set_style())

        elif sheetname.row_values(row)[1] == '审批' and sheetname.row_values(row)[8] == 'Y':
            try:
                data = test_dbZdjknsr(sheetname.row_values(row))

            except Exception as e:
                sheet1.write(row, 9, 'Fail', set_style())
                sheet1.write(row, 10, str(e), set_style())
                continue
            else:

                sheet1.write(row, 9, data[9], set_style())
                sheet1.write(row, 10, data[10], set_style())

        elif sheetname.row_values(row)[1] == '修改' and sheetname.row_values(row)[8] == 'Y':
            try:
                data = test_xgZdjknsr(sheetname.row_values(row))
            except Exception as e:
                sheet1.write(row, 9, 'Fail', set_style())
                sheet1.write(row, 10, str(e), set_style())
                continue
            else:

                sheet1.write(row, 9, data[9], set_style())
                sheet1.write(row, 10, data[10], set_style())

    f.save(r'd:\Lww\py\zdjknsr\conf\test_data_result.xls')


if __name__ == "__main__":
    readXl()
