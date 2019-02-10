#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/10 23:17


# 打印日志

import logging
# 将日志打印到文件中
# 打印日志时需加入format
logging.basicConfig(filename='log.txt',format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s: %(message)s',
                    level=logging.INFO, datefmt='%Y-%m-%d %H:%M:%S')
# Define a Handler and set a format which output to console
# console = logging.StreamHandler()  # 定义console handler
# console.setLevel(logging.INFO)  # 定义该handler级别
# formatter = logging.Formatter('%(asctime)s  %(filename)s : %(levelname)s  %(message)s')  # 定义该handler格式
# console.setFormatter(formatter)
# console.
# # Create an instance
# logging.getLogger().addHandler(console)  # 实例化添加handler

# Print information              # 输出日志级别
logging.debug('logger debug message')
logging.info('logger info message')
logging.warning('logger warning message')
logging.error('logger error message')
logging.critical('logger critical message')


def divide(first, second):
    logging.info('%s / %s' % (first, second))
    return first/second


divide(10, 0)
