#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/1 19:51

import branca
import pandas as pd
import folium
import json
import requests
import webbrowser
from bs4 import BeautifulSoup
import pandas
from folium.plugins import HeatMap
import numpy as np

def get_fake_data():
    num = 100
    new_data = pd.read_csv('country_loc.csv')
    print(new_data)
    # new_data.to_csv('country_loc.csv', ' ')
    lat = np.array(new_data['latitude'][0:num])
    lon = np.array(new_data['longitude'][0:num])
    sim_data = np.array(new_data['sim_data'][0:num], dtype=float)
    return [[lat[i], lon[i], sim_data[i]] for i in range(num)]

def gen_heat_map(data):
    map_osm = folium.Map(location=[-10, 50], zoom_start=5)
    HeatMap(data).add_to(map_osm)

    file_path = r'heatmap17.html'
    map_osm.save(file_path)

    webbrowser.open(file_path)

if __name__ == '__main__':
    data = get_fake_data()
    print(data)
    gen_heat_map(data)
