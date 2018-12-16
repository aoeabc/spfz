#encoding=utf-8
from action.PageAction import *
from util.ParserExcel import ParserExcel
from conf.VarConfig import *
from testScripts.WriteTestResult import writeTestResult
import time
import traceback
import sys

def dataDriverFunc():
    try:
        #  获取名为“测试用例”的sheet对象
        caseSheet = ParserExcel(sheet_name="测试用例")
        #  获取测试用例是否执行列数据
        isRun = caseSheet.get_cols_data(case_is_run)
        #  记录执行成功的测试用例个数
        successfulCase = 0
        #   需要执行的用例个数
        isRunCase = 0
        # idx从0开始计数
        for idx, i in enumerate(isRun[1:]):
            #  判断是否执行
            if i.lower()=="y":
                isRunCase += 1
                #   获取用例表中，执用例步骤的sheet名
                stepSheetName = caseSheet.get_cell_value(row=idx+1,col=case_funcname )


                #   实例化sheet名称
                caseStepObj = ParserExcel(sheet_name=stepSheetName)
                stepNum = caseStepObj.get_lines()
                print(stepNum)

    except Exception as e:
        raise e


if __name__=="__main__":
    dataDriverFunc()