import xlwt
import xlrd
from xlutils.copy import copy


class ParserExcel:

    def __init__(self):
        self.workbook = None
        self.excelFile = None
        self.font = Font(color=None)
        self.RGBDict = {'red': 'FFFF3030', 'green':'FF008B00'}

    def loadWorkBook(self,excelfile):
        # 根据路径获取表格对象
        try:
            self.workbook =  xlrd.open_workbook(excelfile)
        except Exception as e:
            raise e
        self.excelFile = excelfile
        return self.workbook

    def getSheetByName(self, sheetname):
        #  根据sheet表名获取工作表对象
        try:
            sheet = self.workbook.sheet_by_name(sheetname)
            return sheet
        except Exception as e:
            raise e

    def getSheetByName(self, sheetindex):
        #  根据sheet表索引获取工作表对象
        try:
            sheet = self.workbook.sheet_by_index(sheetindex)
            return sheet
        except Exception as e:
            raise e

    def getRowsNumber(self, sheet):
        #  获取工作表内容行数
        return sheet.nrows

    def getColsNumber(self, sheet):
        # 获取工作表内容列数
        return sheet.ncols

    def getRow(self, sheet, rownumber):
        # 获取某一行的内容
        return sheet.row_values(rownumber-1)

    def getCol(self, sheet, colnumber):
        # 获取某一行的内容
        return sheet.col_values(colnumber-1)
    
