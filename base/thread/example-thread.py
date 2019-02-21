#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/16 21:46

import time, threading


# 新线程执行的代码：
def loop():
    print('thread %s is running...' % threading.current_thread().name)
    n = 0
    while n < 5:
        n = n + 1
        print('thread %s >>> %s' %(threading.current_thread().name, n))
        # 当前线程休息1ms
        time.sleep(1)
    print('thread %s ended.' % threading.current_thread().name)


# 当前线程为主线程
print('thread %s is running ...' % threading.current_thread().name)
t = threading.Thread(target=loop, name='LoopThread')
t.start()
t.join()
# 当前线程为主线程
print('thread %s ended' % threading.current_thread().name)
