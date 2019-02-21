#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/16 23:51

from multiprocessing import Pool
import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))


if __name__ == '__main__':
    print('Parent process %s.' % os.getpid())
    # pool的大小为4
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=('test-%s' % i,))
    print('Waiting for all subprocesses done...')
    p.close()  # close之后不能再添加子进程
    p.join()  # join等待所有子进程执行完毕
    print('All subprocesses done.')
