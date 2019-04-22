#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/12 0:10

import logging


# 自己封装的日志处理类，用于统一设置日志处理的格式
class Logger(object):
    def __init__(self, name, file_path, clevel = logging.DEBUG, flevel = logging.DEBUG):
        self.logger = logging.getLogger(name)  # 获得一个命名的日志处理器
        self.logger.setLevel(logging.DEBUG)  # 设置日志的默认级别
        fmt = logging.Formatter('{%(asctime)s] [%(module)s] [%(levelname)s] %(message)s', '%Y-%m-%d %H-%M-%S')  # 获得日志格式

        # cmd日志
        sh = logging.StreamHandler()
        sh.setFormatter(fmt)
        sh.setLevel(clevel)

        # 文件日志
        fh = logging.FileHandler(file_path, encoding='utf-8')
        fh.setFormatter(fmt)
        fh.setLevel(flevel)
        self.logger.addHandler(sh)
        self.logger.addHandler(fh)

    def debug(self, message):
        self.logger.debug(message)

    def info(self, message):
        self.logger.info(message)

    def warning(self, message):
        self.logger.warning(message)

    def error(self, message):
        self.logger.error(message)

    def critical(self, message):
        self.logger.critical(message)


if __name__ == '__main__':
    logger = Logger('test', 'test.log')
    logger.debug('hello')
