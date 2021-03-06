import xlrd
from xlutils.copy import copy
from util.DirAndTime import *
from conf.VarConfig import *


class ParserExcel:

	def __init__(self,sheet_name,file_name=None):
		self.sheet_name = sheet_name
		if file_name:
			self.file_name = file_name
		else:
			self.file_name = dateFilePath

		self.data = self.get_data()

	#获取sheets的内容
	def get_data(self):
		data = xlrd.open_workbook(self.file_name)
		tables = data.sheet_by_name(self.sheet_name)
		return tables

	#获取单元格的行数
	def get_lines(self):
		tables = self.data
		return tables.nrows

	#获取某一个单元格的内容
	def get_cell_value(self,row,col):
		return self.data.cell_value(row,col)

	#写入数据
	def write_value(self,row,col,value):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data=write_data.get_sheet(write_data.sheet_index(self.sheet_name))
		sheet_data.write(row,col,value)
		write_data.save(self.file_name)

	# 写入当前时间
	def write_current_time(self,row,col):
		'''
		写入excel数据
		row,col,value
		'''
		read_data = xlrd.open_workbook(self.file_name)
		write_data = copy(read_data)
		sheet_data = write_data.get_sheet(write_data.sheet_index(self.sheet_name))
		sheet_data.write(row,col,str(getCurrentTime()))
		write_data.save(self.file_name)

	#根据对应的caseid(唯一标识) 找到对应行的内容
	def get_rows_data(self,case_id):
		row_num = self.get_row_num(case_id)
		rows_data = self.get_row_values(row_num)
		return rows_data

	#根据对应的caseid找到对应的行号
	def get_row_num(self,case_id):
		num = 0
		cols_data = self.get_cols_data()
		for col_data in cols_data:
			if str(case_id) in col_data:
				return num
			num = num+1


	#根据行号，找到该行的内容
	def get_row_values(self,row):
		tables = self.data
		row_data = tables.row_values(row)
		return row_data

	#获取某一列的内容
	def get_cols_data(self,col_id=None):
		if col_id != None:
			cols = self.data.col_values(col_id)
		else:
			cols = self.data.col_values(0)
		return cols


if __name__ == '__main__':
    opers = ParserExcel(sheet_name="用例登录")
    s='任务分配'
    print(opers.get_row_num(s))
