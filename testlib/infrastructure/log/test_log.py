#encoding: utf-8
import os
import datetime
import logging
from logging.handlers import RotatingFileHandler
log_path = os.path.split(os.path.realpath(__file__))[0]


class NormalFilter(logging.Filter):
    def __init__(self, level):
        super(NormalFilter, self).__init__()
        self.level = level

    def filter(self, record):
        return record.levelno < self.level


class TestLog(object):

    def __init__(self):
        self.path = log_path
        self.cfg_logging()

    def cfg_logging(self, log_level=logging.INFO):
        current = self.path
        logging.basicConfig(level=log_level)
        logger = logging.getLogger()
        if len(logger.handlers) > 1:
            return
        formatter = logging.Formatter('[%(asctime)s][%(levelname)s][%(threadName)s] %(message)s')
        error_info_handler = logger.handlers[0]
        error_info_handler.setFormatter(formatter)
        error_info_handler.setLevel(log_level)
        file_handler = RotatingFileHandler(filename='{0}/TestLog_{1}.log'.format(current,
            datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S')), maxBytes=10*1024*1024, backupCount=10)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)