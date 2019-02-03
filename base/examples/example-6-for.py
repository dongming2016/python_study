#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/1/9 21:31

'''
python中的循环有两种
for in
while
'''

for i in [1, 2, 3]:
    print(i)

j = 0
while j < 10:
    print(j)
    j += 1

k = 0
while True:
    print('k0:', k)
    k += 1
    if k > 3:
        break  # 终止当前层循环

print('\r')
l = 0
while l < 2:
    l += 1
    k = 0
    while True:
        print('k1:', k)
        k += 1
        if k > 3:
            break  # 终止当前层循环

m = sum1 = 0
print('\r')
while m < 100:
    m += 1
    if m % 2:
        sum1 += m
    else:
        continue  # continue跳过本次循环

print(sum1)

