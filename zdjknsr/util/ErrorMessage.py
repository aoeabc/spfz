import os
class FuncMessage:

    def __init__(self,functionname):
        self.functionname=functionname
        self.funcflag=''
        self.funclog=[]

    def ErrorMessage(self, errormsg=''):

        if errormsg != '':
            self.funcflag='Fail'
            self.funclog.append(errormsg)

        else:
            self.funcflag='Pass'

    def FuncMessage(self,message):
        self.funclog.append(message)


    def WtMessage(self):
        f=open(r'd:/log.txt','wd')
        f.write(self.functionname)
        f.write(self.funclog)


