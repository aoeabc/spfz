from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
import time



class CommonAction:

    @staticmethod
    def checkbox(driver,id,element):
        try:

            querytable = ZdjknsrQueryPage(driver)

            while 'mini-buttonedit-popup' not in querytable.checkboxObj(id).get_attribute("class"):

                element.click()
                if 'mini-buttonedit-popup' in querytable.checkboxObj(id).get_attribute("class"):
                    break
        except Exception as e:
            raise e


    @staticmethod
    def putPsry(driver, spry,id):
        try:

            tablepage = ZdjknsrTablePage(driver)
            time.sleep(5)
            CommonAction.checkbox(driver, id, tablepage.nextPsrySBtnObj(id))
            tablepage.nextPsryObj(spry).click()
            tablepage.nextPsryBtnObj().click()
            time.sleep(3)
            message=tablepage.tjMessageObj().get_attribute('innerText')
            assert '成功' in message
            tablepage.tjMessageBtnObj().click()
            time.sleep(3)

        except Exception as e:
            raise e

