#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/3/26 14:19

import tabula
# try:
# t = tabula.read_pdf('第二部分中国2012年投入产出表_省略_投入产出表_产品部门_产品部门_程子林主.pdf', encoding='utf8', pages=2, area=(406, 24, 695, 589))
# print(t)
# except UnicodeDecodeError as e:
#     print(e)

# tabula.convert_into('第二部分中国2012年投入产出表_省略_投入产出表_产品部门_产品部门_程子林主.pdf', "output.csv", output_format="csv")
# print(t)
import pdfplumber
# with pdfplumber.open("第一部分中国2012年投入产出表_省略_中国2012年投入产出表编制流程_程子林.pdf") as pdf:
# with pdfplumber.open("第二部分中国2012年投入产出表_省略_投入产出表_产品部门_产品部门_程子林主.pdf") as pdf:
#     p = pdf.pages[3]
#     print(p.extract_text())

# import pyocr

import importlib

import sys

import time
import re

importlib.reload(sys)

time1 = time.time()

# print("初始时间为：",time1)


import os.path

from pdfminer.pdfparser import PDFParser
from pdfminer.pdfdocument import PDFDocument, PDFTextExtractionNotAllowed
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage

from pdfminer.converter import PDFPageAggregator

from pdfminer.layout import LTTextBoxHorizontal, LAParams

# from pdfminer.pdfinterp import PDFTextExtractionNotAllowed

text_path = r'words-words.pdf'


# text_path = r'photo-words.pdf'


def parse(text_path):
    '''解析PDF文本，并保存到TXT文件中'''

    fp = open(text_path, 'rb')

    # 用文件对象创建一个PDF文档分析器

    parser = PDFParser(fp)

    document = PDFDocument(parser)
    # 检查文件是否允许文本提取
    if not document.is_extractable:
        raise PDFTextExtractionNotAllowed
    # 创建一个PDF资源管理器对象来存储共享资源
    # caching = False不缓存
    rsrcmgr = PDFResourceManager(caching=False)
    # 创建一个PDF设备对象
    laparams = LAParams()
    # 创建一个PDF页面聚合对象
    device = PDFPageAggregator(rsrcmgr, laparams=laparams)
    # 创建一个PDF解析器对象
    interpreter = PDFPageInterpreter(rsrcmgr, device)
    # 处理文档当中的每个页面

    # doc.get_pages() 获取page列表
    # for i, page in enumerate(document.get_pages()):
    # PDFPage.create_pages(document) 获取page列表的另一种方式
    replace = re.compile(r'\s+');
    # 循环遍历列表，每次处理一个page的内容
    for page in PDFPage.create_pages(document):
        interpreter.process_page(page)
        # 接受该页面的LTPage对象
        layout = device.get_result()
        # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
        # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
        for x in layout:
            # 如果x是水平文本对象的话
            if (isinstance(x, LTTextBoxHorizontal)):
                text = re.sub(replace, '', x.get_text())
                if len(text) != 0:
                    try:
                        print(text.encode('utf8').decode('utf8'))
                    except UnicodeEncodeError as e:
                        print(e)

if __name__ == '__main__':
    parse('第二部分中国2012年投入产出表_省略_投入产出表_产品部门_产品部门_程子林主.pdf')

    time2 = time.time()

    print("总共消耗时间为:", time2 - time1)