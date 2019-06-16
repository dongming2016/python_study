#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/3 15:42

import folium.features as features
import pandas as pd

new_data = pd.read_csv('country_loc.csv')
columns = ['latitude', 'longitude', 'name', 'sim_data']
m = features.Choropleth(data=new_data ,columns=columns,key_on = 'name')


m.save('test.html')

