from pageObjects.ZdjknsrQueryPage import ZdjknsrQueryPage


class CommonAction:

    @staticmethod
    def checkbox(driver,id,element):
        querytable = ZdjknsrQueryPage(driver)

        while 'mini-buttonedit-popup' not in querytable.checkboxObj(id).get_attribute("class"):

            element.click()
            if 'mini-buttonedit-popup' in querytable.checkboxObj(id).get_attribute("class"):
                break