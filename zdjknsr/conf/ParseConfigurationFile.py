from configparser import ConfigParser
from conf.VarConfig import pageElementLocatorPath


class ParseConfigFile:

    def __init__(self):
        self.cf = ConfigParser()
        self.cf.read(pageElementLocatorPath)

    def getItemsSection(self, sectionName):
        optionDict = dict(self.cf.items(sectionName))
        return optionDict

    def getOptionValue(self, sectionName, optionName):
        value = self.cf.get(sectionName, optionName)
        return value

if __name__=='__main__':
    pc = ParseConfigFile()
    dit=pc.getItemsSection('LoginPage')
    print(dit['usernameobj'])
    print(pc.getItemsSection('LoginPage'))
    print(pc.getOptionValue('LoginPage', 'userNameObj'))