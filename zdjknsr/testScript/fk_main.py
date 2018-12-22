from appModules.ExcelAction import ExcelAction
from appModules.FkRwdyAction import *
from appModules.FkRwxfAction import *
from appModules.FkRwfpAction import *
from appModules.FkRwfkAction import *
from appModules.FkRwfkfhAction import *
from appModules.FkRwfktzAction import *
from appModules.FkRwfktzspAction import *
from appModules.LoginTree import LoginTree
from appModules.TreeAction import TreeAction

class FkMain:
    def __init__(self):
        self.get_data = ExcelAction()



    def main_run(self):
        rows = self.get_data.get_sheet_lines()
        for rowid in range(0,rows):
