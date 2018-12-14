#encoding=utf-8
from action.PageAction import *
from util.ParserExcel import ParserExcel
from conf.VarConfig import *
from testScripts.WriteTestResult import writeTestResult
import time

def dataLoginToTree():
    try:
        #  实例化登录步骤sheet页面
        sheetObj = ParserExcel(sheet_name="登录步骤")



    except Exception as e:
        raise e

if __name__ == '__main__':
    dataLoginToTree("任务定义")