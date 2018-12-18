#encoding=utf-8
from action.PageAction import *
from util.ParserExcel import ParserExcel
from conf.VarConfig import *
from testScripts.WriteTestResult import writeTestResult
from testScripts.DataLoginToTree import dataLoginToTree
from testScripts.GetDataInSheet import getDataInSheet
from util.Log import *
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
                logging.info(u"开始执行测试用例'%s'" %stepSheetName)
                #    登录系统并进入测试页面
                dataLoginToTree(stepSheetName)
                #   实例化sheet名称
                caseStepObj = ParserExcel(sheet_name=stepSheetName)
                #   获取用例步骤行数
                stepNum = caseStepObj.get_lines()
                successfulStep = 0
                for index in range(1,stepNum):
                    #  获取每一行的数据
                    stepRow = caseStepObj.get_row_values(index)
                    #  获取当前行的关键字
                    keyWord = stepRow[step_keyword]
                    #   获取当前行关键字的定位方式
                    locationType = stepRow[step_location_type]
                    #   获取定位表达式
                    locationExpression = getDataInSheet(stepRow[step_location_expression], stepSheetName)
                    #   获取操作值
                    operateValue = getDataInSheet(stepRow[step_value], stepSheetName)
                    #   拼接定位方式和表达式
                    tmpStr = "'%s',\"%s\"" % (locationType.lower(), locationExpression) \
                        if locationType and locationExpression else ""
                    #   拼接操作值
                    if tmpStr:
                        tmpStr += ",u'" + operateValue + "'" if operateValue else ""
                    else:
                        tmpStr += "u'" + operateValue + "'" if operateValue else ""
                    #   拼接关键字，
                    runStr = keyWord + "(" + tmpStr + ")"
                    logging.info(u"开始执行测试步骤命令：%s" % runStr)
                    try:
                        #  将字符串转化成有效表达式
                        eval(runStr)
                    except Exception as e:
                        logging.info(u"执行步骤'%s'发生异常" % stepRow[step_message])
                        capturePic = capture_screen()
                        errorInfo = traceback.format_exc()
                        writeTestResult(sheetName=stepSheetName,
                                        rowNo=index,
                                        ColsNo="testStep",
                                        testResult="faild",
                                        errorMes=str(errorInfo),
                                        PicPath=capturePic)
                    else:
                        successfulStep += 1
                        logging.info(u"执行步骤'%s'成功" % stepRow[step_message])
                        writeTestResult(sheetName=stepSheetName,
                                        rowNo=index,
                                        ColsNo="testStep",
                                        testResult="pass")
                if successfulStep == stepNum - 1:
                    successfulCase += 1
                    logging.info(u"%s功能执行成功" %stepSheetName)
                    writeTestResult(sheetName="测试用例",
                                    rowNo=caseSheet.get_row_num(stepSheetName),
                                    ColsNo="testCase",
                                    testResult="pass")
                else:
                    logging.info(u"进入%s页面失败" % stepSheetName)
                    writeTestResult(sheetName="测试用例",
                                    rowNo=caseSheet.get_row_num(stepSheetName),
                                    ColsNo="testCase",
                                    testResult="fail")
            else:
                writeTestResult(sheetName="测试用例",
                                rowNo=caseSheet.get_row_num(stepSheetName),
                                ColsNo="testCase",
                                testResult="")

        logging.info(u"共%d条用例，执行%d条，成功执行%d条" %(len(isRun,)-1),isRunCase,successfulCase)

    except Exception as e:
        logging.debug(u"程序执行异常\n%s " % traceback.print_exc())

if __name__=="__main__":
    dataDriverFunc()