#encoding=utf-8
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class WaitUtil:
    def __init__(self, driver):
        self.locationTypeDict = {
            "xpath":By.XPATH,
            "id":By.ID,
            "css_selector":By.CSS_SELECTOR,
            "name":By.NAME,
            "tag_name":By.TAG_NAME,
            "class_name":By.CLASS_NAME
        }
        self.driver = driver
        self.wait = WebDriverWait(self.driver)

    def presenceOfElementLocated(self, located_method, located_expression, *arg):
        '''显示等待页面元素出现在DOM中，并不一定可见，存在则返回页面元素对象'''
        try:
            if self.locationTypeDict.has_key(located_method.lower()):
                element = self.wait.util(\
                    EC.presence_of_element_located(\
                        self.locationTypeDict[located_method.lower()],located_expression))
                return element
            else:
                raise TypeError(u"未找到定位方式，请确认定位方法是否正确")
        except Exception as e:
            raise e

    def frameToBeAvailableAndSwitchToIt(self, located_method, located_expression, *arg):
        '''检查frame是否存在，存在就切换进去'''
        try:
            element = self.wait.util(\
                EC.frame_to_be_available_and_switch_to_it(\
                    self.locationTypeDict[located_method.lower()],located_expression))
            return element

        except Exception as e:
            raise e

    def visibilityOfElementLocated(self, located_method, located_expression, *arg):
        '''检查frame是否存在，存在就切换进去'''
        try:
            element = self.wait.util(\
                EC.visibility_of_element_located(\
                    self.locationTypeDict[located_method.lower()],located_expression))
            return element

        except Exception as e:
            raise e