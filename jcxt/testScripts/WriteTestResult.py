#encoding=utf-8
from util.ParserExcel import ParserExcel
from conf.VarConfig import *
import time
import traceback
import sys


def writeTestResult(sheetName, rowNo, ColsNo, testResult, errorMes=None, PicPath=None):
    sheetObj = ParserExcel(dateFilePath, sheet_name=sheetName)
    colsDict={
        "testCase":[case_time,case_result],
        "testStep":[step_time,step_result],
        "loginStep":[to_tree_time,to_tree_result]
    }
    try:
        # 记录测试步骤结果、时间，
        sheetObj.write_value(row=rowNo,col=colsDict[ColsNo][1],value=testResult)
        if testResult =="":
            sheetObj.write_value(row=rowNo, col=colsDict[ColsNo][0], value="")
        else:
            sheetObj.write_current_time(row=rowNo, col=colsDict[ColsNo][0])

        if errorMes and PicPath:
            sheetObj.write_value(row=rowNo, col=step_error_message, value=errorMes)
            sheetObj.write_value(row=rowNo, col=step_error_pic, value=PicPath)
        else:
            if ColsNo =="testCase":
                sheetObj.write_value(row=rowNo, col=step_error_message, value="")
                sheetObj.write_value(row=rowNo, col=step_error_pic, value="")
    except Exception as e:
        print("写入数据时发生错误")
        print(traceback.print_exc())
