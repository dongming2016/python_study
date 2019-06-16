#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#from selenium import webdriver
from pyquery import PyQuery as pq
import json
import pandas as pd
import time
from selenium.webdriver import Chrome
from selenium.webdriver import ChromeOptions
option = ChromeOptions()
option.add_experimental_option('excludeSwitches', ['enable-automation'])
driver = Chrome(options=option)
url='http://www.mee.gov.cn/xxgklssj'
driver.get(url)
content=driver.page_source
driver.switch_to.frame('myiframe')
input_0=driver.find_elements_by_css_selector('.iframe-box .iframe-list')
time.sleep(20)
print(input_0)

