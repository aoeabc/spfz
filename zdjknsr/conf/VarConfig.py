import os

# 当前文件的父目录的局对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# 页面元素定位表达式绝对路径
pageElementLocatorPath = parentDirPath + u"\\conf\\PageElementLocator.ini"

# -----------------------重点监控纳税人手动出库----------------
# 重点监控纳税人手动出库模块测试文档
zdjkdateFilePath = parentDirPath + u"\\conf\\test_data.xlsx"

# testdata.xls文档中每列对应的序列,从0 开始计数，
zdjk_funcname =1
zdjk_url = 2
zdjk_username_pwd = 3
zdjk_firsttree = 4
zdjk_secondtree = 5
zdjk_thirdtree = 6
zdjk_parameter = 7
zdjk_is_run = 8
zdjk_result = 9
zdjk_result_parameter = 10


# -----------------------风险管理系统----------------
fkdateFilePath = parentDirPath + u"\\conf\\fk_data.xls"

#风控文档fk_data.xlsx文档中每列对应的序列,从0 开始计数，
fk_funcname =1
fk_url = 2
fk_username_pwd = 3
fk_firsttree = 4
fk_secondtree = 5
fk_thirdtree = 6
fk_parameter = 7
fk_is_run = 8
fk_result = 9
fk_result_parameter = 10
















