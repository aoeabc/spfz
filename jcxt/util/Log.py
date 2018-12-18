#encoding=utf-8
import logging
import logging.config
from conf.VarConfig import parentDirPath

# 读取日志配置文件
logging.config.fileConfig(parentDirPath + u"\conf\Logger.conf")
logger = logging.getLogger("example02")

def debug(message):
    logger.debug(message)

def info(message):
    logger.info(message)

def warning(message):
    logger.warning(message)