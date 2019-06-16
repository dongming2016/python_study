#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/4/11 14:50
import re
book_list_format = r'[%d]%s,%s[M].%s:%s,%s.'
book_list_format1 = r'[%d]%s,%s[Z].%s:%s,%s.'


import pandas as pd


# 先用pd.cut分段，并取出分段数值
# 通过 precision 控制小数的位数
def read_data(path):
    return pd.read_excel(path)

def format_data(data):

    name, publisher, location, time1, author = data['书名'], data['出版社'], data['地点'], data['出版日期'], data['作者']
    # print(name, publisher,location, time, author
    # print(time1)
    count = 0
    # print()
    for n in name:
        c = count + 1
        try:
            # print(time1[count])
            if author[count] not in ['王伟光', '任仲文', '柳斌杰', '何毅亭', '许海清']:
                b = book_list_format1 % (c, author[count], n, location[count], publisher[count], re.findall(r'\d\d\d\d', time1[count])[0])
            else:
                b = book_list_format % (c, author[count], n, location[count], publisher[count],
                                        re.findall(r'\d\d\d\d', time1[count])[0])
        except:
            b = book_list_format % (c, author[count], n, location[count], publisher[count],
                                    '')
        print(b.replace('nan,', '').replace('nan:', ''))
        count += 1
    # book_list_format % ()

if __name__ == '__main__':
    data = read_data('C:/Users/35037/Desktop/论文/习近平高质量发展思想/习近平书录1.xlsx')
    format_data(data)
