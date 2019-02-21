#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/21 20:15

# 进程之间变量是不共享上下文的。
# 而线程之间是共享上下文的。

import time, threading

# 银行存款
balance = 0
lock = threading.Lock()


# 多线程产生错误的原因是：1.线程间共用同一个数据；2.对同一个数据进行修改操作。
# 解决办法之一是加锁
def change_it(n):
    # 先存后取
    global balance  # 全局变量
    # 这一段代码执行的是两个操作，增加和赋值的操作，中间因为线程会相互切换，因此可能会产生错误。
    balance += n
    balance -= n
    # 预期应该是为0


def run_thread(n):
    for i in range(1000000):
        # 获得锁
        lock.acquire()
        try:
            change_it(n)
        finally:
            # 释放锁
            lock.release()


t1 = threading.Thread(target=run_thread, args=(5, ))
t2 = threading.Thread(target=run_thread, args=(8, ))
t1.start()
t2.start()
t1.join()
t2.join()
print(balance)
