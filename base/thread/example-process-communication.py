#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/21 19:54

# 进程之间通信
from multiprocessing import  Process, Queue
import  os, time, random


# 写入数据:
def write(q):
    print('Process to write: %s' % os.getpid())
    for value in ['A', 'B', 'C']:
        print('Pit %s to queue...' % value)
        q.put(value)
        time.sleep(random.random())


# 读数据进程执行的代码。同一变量并不共享。
def read(q):
    print('Process to read: %s' % os.getpid())
    while True:
        value = q.get(True)
        print('Get %s from queue.' % value)


if __name__ == '__main__':
    # 父进程创建Queue，并传给子进程
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q, ))
    # 启动子进程pw，写入
    pw.start()
    # 启动子进程pr，读取
    pr.start()
    # 等待pw结束：
    pw.join()
    # 强制结束pr进程
    pr.terminate()
