import logging

from utils.VerifyUtils import VerifyUtils
from utils.log.LogUtils import LogUtils


class TimerUtils():
    def __init__(self):
        LogUtils.init_logger()
        logging.info("this is a log test")
        logging.warning("this is a awrnm test")
        VerifyUtils().test_log()


if __name__ == '__main__':
   TimerUtils()