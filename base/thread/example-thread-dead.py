#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/21 20:30
import threading,multiprocessing


# python必须先获得GIL锁，global interpreter lock，每执行100行字节码便会释放锁，
# 因此无法通过多线程实现真正的多任务
def loop():
    x = 0
    while True:
        x = x ^ 1


for i in range(multiprocessing.cpu_count()):
    t = threading.Thread(target=loop())
    t.start()
