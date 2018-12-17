#encoding=utf-8
from selenium import webdriver
from util.ObjectMap import getElement
from util.DirAndTime import *
from  util.WaitUtil import WaitUtil
import time

driver = None
waitUtil = None

def open_browser():
    #  打开浏览器
    global driver,waitUtil
    try:
        driver = webdriver.Ie()
        waitUtil = WaitUtil(driver)
    except Exception as e:
        raise e

def visit_url(url, * arg):
    #  访问地址
    global driver
    try:
        driver.get(url)
        handles = driver.window_handles
        driver.switch_to.window(handles[0])
    except Exception as e:
        raise e

def close_browser(* arg):
    #  关闭浏览器
    global driver
    try:
        driver.qiut()
    except Exception as e:
        raise e

def sleep(sleepSeconds, * arg):
    #  延时等到
    try:
        time.sleep(int(str(sleepSeconds)[0:1]))
    except Exception as e:
        raise e

def clear(locationType, locationExpression, * arg):
    #  清空输入框
    global driver
    try:
        getElement(driver, locationType, locationExpression).clear()
    except Exception as e:
        raise e

def input_string(locationType, locationExpression, contant):
    #  输入框输入数据
    global driver
    try:
        getElement(driver, locationType, locationExpression).send_keys(contant)
    except Exception as e:
        raise e

def click(locationType, locationExpression):
    #  输入框输入数据
    global driver
    try:
        getElement(driver, locationType, locationExpression).click()
    except Exception as e:
        raise e

def scroll_to(locationType, locationExpression):
    #  输入框输入数据
    global driver
    try:
        driver.execute_script("arguments[0].scrollIntoView();", getElement(driver, locationType, locationExpression))
    except Exception as e:
        raise e

def assert_string_in_pagesource(assertString):
    #  判断当前页面中是都存在关键字
    global driver
    try:
        assert assertString in driver.page_source,u"%s 不在当前页面" %assertString
    except AssertionError as e:
        raise e
    except Exception as e:
        raise e

def switch_to_frame(locationType, locationExpression,* arg):
    #  切换到frame
    global driver
    try:
        driver.switch_to.frame(getElement(driver, locationType, locationExpression))
    except Exception as e:
        raise e

def switch_to_default_content(* arg):
    #  切换到默认框
    global driver
    try:
        driver.switch_to.default_content()
    except Exception as e:
        raise e

def capture_screen(* arg):
    #  截图图片
    global driver
    currTime = getCurrentTime()
    picNameAndPath = str(creatCurrentDataDir()+"\\"+str(currTime)+".png")
    try:
        driver.get_screenshot_as_file(picNameAndPath.replace('\\',r'\\'))
    except Exception as e:
        raise e
    else:
        return picNameAndPath

def waitPresenceOfElementLocated(locationType, locationExpression,* arg):
    '''显式等待页面元素出现在DOM中，但并不一定可见，存在则返回页面元素对象'''
    global waitUtil
    try:
        waitUtil.presenceOfElementLocated(locationType, locationExpression)
    except Exception as e:
        raise e

def waitframeToBeAvailableAndSwitchToIt(locationType, locationExpression,* arg):
    '''检查frame是否存在，存在则切换到frame中'''
    global waitUtil
    try:
        waitUtil.frameToBeAvailableAndSwitchToIt(locationType, locationExpression)
    except Exception as e:
        raise e

def waitvisibilityOfElementLocated(locationType, locationExpression,* arg):
    '''检查frame是否存在，存在则切换到frame中'''
    global waitUtil
    try:
        waitUtil.visibilityOfElementLocated(locationType, locationExpression)
    except Exception as e:
        raise e