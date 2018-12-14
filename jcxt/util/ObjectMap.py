#encoding=utf-8
from selenium.webdriver.support.ui import WebDriverWait

def getElement(driver,locateType,locatorExpression):
    try:
        element=WebDriverWait(driver,30).until\
                 (lambda x:x.find_element(by=locateType,value=locatorExpression))
        return element
    except Exception as e:
        raise e

def getElements(driver,locateType,locatorExpression):
    try:
        elements=WebDriverWait(driver,30).until\
                  (lambda x:x.find_elements(by=locateType,value=locatorExpression))
        return elements
    except Exception as e:
        raise e

