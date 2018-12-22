from conf.ParserExcel import *
from conf.VarConfig import *


class ExcelAction:
    def __init__(self):
        self.excel = ParserExcel()

    def is_run(self, row_num):
        return self.excel.get_cell_value(row_num, fk_is_run)

    def get_url(self, row_num):
        return self.excel.get_cell_value(row_num, fk_url)

    def get_username_pwd(self, row_num):
        username_pwd = self.excel.get_cell_value(row_num, fk_username_pwd)
        username = username_pwd.split(";")[0]
        password = username_pwd.split(";")[1]
        return username,password

    def get_funcname(self, row_num):
        return self.excel.get_cell_value(row_num, fk_funcname)

    def get_first_tree(self, row_num):
        return self.excel.get_cell_value(row_num, fk_firsttree)

    def get_second_tree(self, row_num):
        return self.excel.get_cell_value(row_num, fk_secondtree)

    def get_third_tree(self, row_num):
        return self.excel.get_cell_value(row_num, fk_thirdtree)

    def get_parameter(self, row_num):
        return  self.excel.get_cell_value(row_num, fk_parameter)

    def set_result(self, row_num, result):
        self.excel.write_value(row_num, fk_result, result)

    def set_result_parameter(self, row_num, result):
        self.excel.write_value(row_num, fk_result_parameter, result)

    def get_sheet_lines(self):
        return self.excel.get_lines()

if __name__ =="__main__":
    excel = ExcelAction()
    u,p = excel.get_username_pwd(1)


