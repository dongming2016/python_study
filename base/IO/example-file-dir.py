#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/2/15 23:02


# 获取操作系统的信息
import os
from datetime import datetime

# 打印环境变量信息，为一个字典
print(os.environ)
print(os.environ.get('ALLUSERSPROFILE'))
# 获取当前文件所在绝对路径
print(os.path.abspath('.'))
# 创建目录
# os.mkdir('testdir')
# 删掉目录
# os.rmdir('testdir')
# 路径拼接，用join可以屏蔽linux/unix/mac与windows的差异
print(os.path.join('abc', 'dec'))
# 拆分路径,第二个参数时最外层路径
print(os.path.split('/abc/ed/efc'))
# 获取文件扩展名
print(os.path.splitext('/abc/sdfe/a.txt'))

# 列出当前目录下所有的python文件
print([x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1] == '.py'])

pwd = os.path.abspath('.')
print(' Size Last Modified Name')
print('------------------------------------------')

# 列出文件大小，文件修改日期，文件名称
for f in os.listdir(pwd):
    fsize = os.path.getsize(f)
    mtime = datetime.fromtimestamp(os.path.getatime(f)).strftime('%Y-%m-%d %H:%M')  # strftime格式化时间
    flag = '/' if os.path.isdir(f) else ''
    print('%10d  %s  %s%s' % (fsize, mtime, f, flag))


# import shutil
# copy文件
# shutil.copy('example-file-dir.py', 'example-f')

