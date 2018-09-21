from selenium import webdriver
import unittest
from HTMLTestRunner import HTMLTestRunner
from testScript import TestAdd


class Baidu(unittest.TestCase):
    def __init__(self, *args, **kwargs):
        unittest.TestCase.__init__(self, *args, **kwargs)

    def setUp(self):
        print('测试开始--------')

    def test_baidu_search(self):
        #pcbh = TestAdd.test_addZdjknsr()
        pcbh =['JCBASJ20180110', 'JCBASJ20180108']
        TestAdd.test_dbZdjknsr(pcbh)

    def tearDown(self):
        print('测试结束--------')


if __name__ == '__main__':
    testsuit = unittest.TestSuite()
    testsuit.addTest(Baidu('test_baidu_search'))
    fp = open(r'd:\\result.html', 'wb')
    runner = HTMLTestRunner(stream=fp, title='重点监控纳税人手动出库', description='用例执行情况')
    runner.run(testsuit)
    fp.close()

