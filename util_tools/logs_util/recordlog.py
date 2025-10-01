#-*- coding:utf-8 -*-
import logging
import os
import time
import colorlog
from logging.handlers import RotatingFileHandler

from config.setting import FILE_PATH

log_path = FILE_PATH['log'] # os.path.join(DIR_PATH, 'log')

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

# # -*- coding:utf-8 -*-
# import logging
# import os
# import time
# import colorlog
# import atexit
# from logging.handlers import RotatingFileHandler, QueueHandler, QueueListener
# import multiprocessing
#
# from config.setting import FILE_PATH
#
# log_path = FILE_PATH['log']
#
# if not os.path.exists(log_path):
#     os.makedirs(log_path, exist_ok=True)
#
# log_file_name = os.path.join(log_path, r'test_{}.log'.format(time.strftime('%Y%m%d')))
# log_err_file_name = os.path.join(log_path, r'test_{}_err.log'.format(time.strftime('%Y%m%d')))
#
# # 全局队列和监听器
# _log_queue = None
# _listener = None
#
#
# def setup_logging_system():
#     """设置进程安全的日志系统"""
#     global _log_queue, _listener
#
#     # 创建进程安全的队列
#     _log_queue = multiprocessing.Queue(-1)
#
#     # 创建文件处理器
#     fh = RotatingFileHandler(
#         log_file_name,
#         mode='a',
#         maxBytes=5242880,
#         backupCount=7,
#         encoding='utf-8'
#     )
#     fh.setLevel(logging.DEBUG)
#
#     fh_err = RotatingFileHandler(
#         log_err_file_name,
#         mode='a',
#         maxBytes=5242880,
#         backupCount=7,
#         encoding='utf-8'
#     )
#     fh_err.setLevel(logging.ERROR)
#
#     # 设置格式化器（添加进程ID）
#     log_formatter = logging.Formatter(
#         '[PID:%(process)d] - %(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(module)s:%(funcName)s - %(message)s'
#     )
#     fh.setFormatter(log_formatter)
#     fh_err.setFormatter(log_formatter)
#
#     # 创建队列监听器
#     _listener = QueueListener(_log_queue, fh, fh_err)
#     _listener.start()
#
#     return _log_queue
#
#
# def stop_log_listener():
#     """安全停止日志监听器"""
#     global _listener
#     if _listener:
#         try:
#             _listener.stop()
#         except:
#             pass
#
#
# # 注册退出时的清理函数
# atexit.register(stop_log_listener)
#
#
# class HandleLogs:
#     @classmethod
#     def log_color(cls):
#         log_color_config = {
#             'DEBUG': 'cyan',
#             'INFO': 'green',
#             'WARNING': 'yellow',
#             'ERROR': 'red',
#             'CRITICAL': 'red'
#         }
#         formatter = colorlog.ColoredFormatter(
#             '%(log_color)s[PID:%(process)d] - %(levelname)s - %(asctime)s - %(filename)s:%(lineno)d - %(funcName)s - %(message)s',
#             log_colors=log_color_config
#         )
#         return formatter
#
#     @classmethod
#     def output_logs(cls):
#         global _log_queue
#
#         # 如果队列未初始化，则初始化
#         if _log_queue is None:
#             _log_queue = setup_logging_system()
#
#         # 使用进程ID创建唯一的logger名称
#         process_id = os.getpid()
#         logger_name = f'process_{process_id}'
#         logger = logging.getLogger(logger_name)
#
#         # 如果logger已经有处理器，直接返回
#         if logger.handlers:
#             return logger
#
#         logger.setLevel(logging.DEBUG)
#
#         # 添加队列处理器（用于文件日志）
#         queue_handler = QueueHandler(_log_queue)
#         queue_handler.setLevel(logging.DEBUG)
#         logger.addHandler(queue_handler)
#
#         # 控制台处理器（每个进程独立）
#         sh = logging.StreamHandler()
#         sh.setLevel(logging.DEBUG)
#         sh.setFormatter(cls.log_color())
#         logger.addHandler(sh)
#
#         # 防止日志传播到根logger
#         logger.propagate = False
#
#         return logger
#
#
# logs = HandleLogs.output_logs()




if __name__ == '__main__':
    logs.info('hello world')
    logs.debug('hello world')
    logs.warning('hello world')
    logs.error('hello world')
    logs.critical('hello world')


