#encoding=utf-8
from action.PageAction import *
from util.ParserExcel import ParserExcel
from conf.VarConfig import *

def getDataInSheet(rowValue,keyName):
    #   根据当前步骤的关键字，及需要转换的单元格数据，转换数据
    #   返回转换完成的数据
    try:
        dataTag = "$"
        #  判断是否需要去取值
        if dataTag in rowValue:
            cellValueEx = rowValue.split("$")[0]
            cellValueBk = rowValue.split("$")[2]
            #  获取取值的sheet表名称
            dataInSheetName = rowValue.split("$")[1].split(";")[1]
            #   获取取值的列名
            dataInSheetCol = eval(rowValue.split("$")[1].split(";")[2])
            #  实例化取值sheet表对象
            inSheet = ParserExcel(sheet_name=dataInSheetName)
            #  获取该关键字所在行行号
            dataInSheetRow=inSheet.get_row_num(keyName)
            #  获取对应值
            dataInSheetValue = inSheet.get_cell_value(dataInSheetRow,dataInSheetCol)
            #  拼接获取后的值
            cellValue = cellValueEx+dataInSheetValue+cellValueBk

    except Exception as e:
        raise e
    else:
        return cellValue

if __name__ == '__main__':
    getDataInSheet("$TO;用例登录;to_tree_firsttree$", "任务定义")