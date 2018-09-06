from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage
from pageObjects.ZdjknsrTablepage import ZdjknsrTablePage
import time

class CommonAction:

    @staticmethod
    def checkbox(driver,id,element):
        querytable = ZdjknsrQueryPage(driver)

        while 'mini-buttonedit-popup' not in querytable.checkboxObj(id).get_attribute("class"):

            element.click()
            if 'mini-buttonedit-popup' in querytable.checkboxObj(id).get_attribute("class"):
                break


    @staticmethod
    def putPsry(driver, spry,id):
        try:

            tablepage = ZdjknsrTablePage(driver)
            time.sleep(5)
            CommonAction.checkbox(driver, id, tablepage.nextPsrySBtnObj(id))
            tablepage.nextPsryObj(spry).click()
            tablepage.nextPsryBtnObj().click()
            time.sleep(2)
            print(tablepage.tjMessageObj().get_attribute('innerText'))
            tablepage.tjMessageBtnObj().click()
            time.sleep(3)

        except Exception as e:
            print(e)

