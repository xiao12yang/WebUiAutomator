#-*- coding:utf-8 -*-
import logging
import os
import time
import colorlog
from logging.handlers import RotatingFileHandler

from config.setting import FILE_PATH

log_path = FILE_PATH['log']

if not os.path.exists(log_path):
    os.mkdir(log_path)

log_file_name = log_path + r'\test_{}.log'.format(time.strftime('%Y%m%d'))
log_err_file_name = log_path + r'\test_{}_err.log'.format(time.strftime('%Y%m%d'))

class HandleLogs:
    @classmethod
    def log_color(cls):
        log_color_config = {
            'DEBUG': 'cyan',
            'INFO': 'green',
            'WARNING': 'yellow',
            'ERROR': 'red',
            'CRITICAL': 'red'
        }
        formatter = colorlog.ColoredFormatter(
            '%(log_color)s - %(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(module)s:%(funcName)s - %(message)s',
            log_colors=log_color_config
        )
        return formatter




    @classmethod
    def output_logs(cls):
        logger = logging.getLogger(__name__)
        if not logger.handlers:
            logger.setLevel(logging.DEBUG)
            log_formatter = logging.Formatter('%(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(module)s:%(funcName)s - %(message)s')

            # 日志输出到控制台
            sh = logging.StreamHandler()
            sh.setLevel(logging.DEBUG)
            sh.setFormatter(cls.log_color())
            logger.addHandler(sh)

            # 日志输出到文件
            fh = RotatingFileHandler(log_file_name,
                                     mode='a',
                                     maxBytes=5242880,
                                     backupCount=7,
                                     encoding='utf-8')
            fh.setLevel(logging.DEBUG)
            fh.setFormatter(log_formatter)
            logger.addHandler(fh)

            fh_err = RotatingFileHandler(log_err_file_name,
                                         mode='a',
                                         maxBytes=5242880,
                                         backupCount=7,
                                         encoding='utf-8')
            fh_err.setLevel(logging.ERROR)
            fh_err.setFormatter(log_formatter)
            logger.addHandler(fh_err)

        return logger

logs = HandleLogs.output_logs()

if __name__ == '__main__':
    logs.info('hello world')
    logs.debug('hello world')
    logs.warning('hello world')
    logs.error('hello world')
    logs.critical('hello world')






