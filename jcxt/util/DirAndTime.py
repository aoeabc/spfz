#encoding=utf-8
import time,os
from datetime import datetime
from conf.VarConfig import screenPicturesDir

# 获取当前日期
def getCurrentDate():
    timeTup = time.localtime()
    currentDate = str(timeTup.tm_year) + "-" + str(timeTup.tm_mon) + "_" + str(timeTup.tm_mday)
    return currentDate

# 获取当前时间
def getCurrentTime():
    timeS = datetime.now()
    currentTime = timeS.strftime("%H-%M-%S-%F")
    return currentTime

def creatCurrentDataDir():
    dirname = os.path.join(screenPicturesDir,getCurrentDate())
    if not os.path.exists(dirname):
        os.makedirs(dirname)
    return dirname