#encoding=utf-8
from action.PageAction import *
from util.ParserExcel import ParserExcel
from conf.VarConfig import *
from testScripts.GetDataInSheet import getDataInSheet
from testScripts.WriteTestResult import writeTestResult
from util.Log import *
import time
import traceback

def dataLoginToTree(keyName):
    try:
        logging.info(u"开始进入%s页面"%keyName)
        #  实例化登录步骤sheet页面
        sheetObj = ParserExcel(sheet_name="登录步骤")
        sheetCaseObj = ParserExcel(sheet_name="用例登录")
        #  获取步骤sheet中的行数
        stepNums = sheetObj.get_lines()
        successfulSteps = 0
        for index in range(1,stepNums):
            #  获取每一行的数据
            stepRow = sheetObj.get_row_values(index)
            #  获取当前行的关键字
            keyWord = stepRow[step_keyword]
            #   获取当前行关键字的定位方式
            locationType = stepRow[step_location_type]
            #   获取定位表达式
            locationExpression = getDataInSheet(stepRow[step_location_expression],keyName)
            #   获取操作值
            operateValue = getDataInSheet(stepRow[step_value],keyName)
            #   拼接定位方式和表达式
            tmpStr = "'%s',\"%s\"" % (locationType.lower(),locationExpression)\
                if locationType and locationExpression else ""
            #   拼接操作值
            if tmpStr:
                tmpStr += ",u'"+operateValue+"'" if operateValue else ""
            else:
                tmpStr += "u'"+operateValue+"'" if operateValue else ""
            #   拼接关键字，
            runStr = keyWord+"("+tmpStr+")"
            logging.info(u"开始执行步骤命令：'%s'" %runStr )
            try:
                #  将字符串转化成有效表达式
                eval(runStr)
            except Exception as e:
                logging.info(u"执行步骤'%s'发生异常" % stepRow[step_message])
                capturePic = capture_screen()
                errorInfo = traceback.format_exc()
                writeTestResult(sheetName="登录步骤",
                                rowNo=index,
                                ColsNo="testStep",
                                testResult="faild",
                                errorMes=str(errorInfo),
                                PicPath=capturePic)
            else:
                successfulSteps += 1
                logging.info(u"执行步骤'%s'成功" % stepRow[step_message])
                writeTestResult(sheetName="登录步骤",
                                rowNo=index,
                                ColsNo="testStep",
                                testResult="pass")
        if successfulSteps == stepNums - 1:
            logging.info(u"登录成功并进入%s页面" %keyName)
            writeTestResult(sheetName="用例登录",
                            rowNo=sheetCaseObj.get_row_num(keyName),
                            ColsNo="loginStep",
                            testResult="pass")
        else:
            logging.info(u"进入%s页面失败" % keyName)
            writeTestResult(sheetName="用例登录",
                            rowNo=sheetCaseObj.get_row_num(keyName),
                            ColsNo="loginStep",
                            testResult="fail")

    except Exception as e:
        logging.debug(u"程序执行异常\n%s " % traceback.print_exc())

if __name__ == '__main__':
    dataLoginToTree("任务定义")