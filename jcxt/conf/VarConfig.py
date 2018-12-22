#encoding=utf-8
import os

# 当前文件的父目录的局对路径
parentDirPath = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

#异常图片存放目录
screenPicturesDir = parentDirPath + "\\exceptionpictures\\"
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
dateFilePath = parentDirPath + "\\testData\\fk_data.xls"

#风控文档fk_data.xlsx文档中，主表每列对应的序列,从0 开始计数，
case_funcname =1
case_parameter = 2
case_is_run = 3
case_time = 4
case_result = 5
case_result_parameter = 6


#风控文档fk_data.xlsx文档中，副表每列对应的序列,从0 开始计数，
step_keyword = 0
step_message = 1
step_location_type = 2
step_location_expression = 3
step_value = 4
step_result = 5
step_time = 6
step_error_message = 7
step_error_pic = 8

#   用例登录sheet中功能的地址及路径
to_tree_func_name=0
to_tree_url = 1
to_tree_username = 2
to_tree_pwd = 3
to_tree_firsttree = 4
to_tree_secondtree = 5
to_tree_thirdtree = 6
to_tree_result = 7
to_tree_time = 8














