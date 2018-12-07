from appModules.LoginAction import LoginAction
from appModules.TreeAction import TreeAction


class LoginTree:

    @staticmethod
    def logintree(url, username, password, ftree, stree, ttree=None):
        try:
            driver = LoginAction.driver(url)
            LoginAction.login(driver, username, password)
            TreeAction.getFirstTree(driver, ftree)
            TreeAction.getSecondTree(driver, stree)
            if ttree != None:
                TreeAction.getThirdTree(driver, ttree)

        except Exception as e:
            raise e

        finally:
            return driver


if __name__ == '__main__':
    url='http://86.100.16.15:8001'
    driver = LoginTree.logintree(url,'szgscaiyj','88881188','重点监控纳税人库','重点监控纳税人手动出库')
    print(driver)
    driver.quit()