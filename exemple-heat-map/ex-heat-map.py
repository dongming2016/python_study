#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/5/31 22:44

import numpy as np
import pandas as pd
import folium
import webbrowser
from folium.plugins import HeatMap

posi = pd.read_excel('2015Cities-CHINA.xlsx')
num = 80
lat = np.array(posi['lat'][0:num])
lon = np.array(posi['lon'][0:num])
pop = np.array(posi['pop'][0:num], dtype=float)
gdp = np.array(posi['GDP'][0:num], dtype=float)
data1 = [[lat[i], lon[i], pop[i]] for i in range(num)]

