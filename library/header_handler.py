#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/4/11 22:25
from functools import reduce

base_path = './%s'

s1 = ' A BC'


def trim(s):
    import re
    if s.startswith(' ') or s.endswith(' '):
        return re.sub(r"^(\s+)|(\s+)$", "", s)
    else:
        return ''

def handle_data(file_name):
    with open(base_path % file_name) as file:
        header_str = file.read()
        head_list = header_str.split('\n')
        headers = {}
        for h in head_list:
            hx = h.split(':')
            v = reduce(lambda x, y: trim(x) + trim(y), hx[1:])
            print(reduce(lambda x,y: x+y, hx[1:]))
            headers[hx[0]] = v
        print(head_list)
        print(file.read())
        print(headers)
        return headers
        # line = file.readable()
        # while line:
        #     print(line)
        #     line = file.readable()

handle_data('header_handler.txt')