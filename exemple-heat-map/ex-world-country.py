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

def get_country_info():
    req = requests.get('https://developers.google.com/public-data/docs/canonical/countries_csv')
    soup = BeautifulSoup(req.text,features="lxml")
    trs = soup.find_all('tr')
    all_data = []
    columns = []
    for td in trs[0]:
        if td == '\n':
            continue
        columns.append(td.string)

    for tr in trs[1:]:
        country = []
        for td in tr.children:
            if td == '\n':
                continue
            country.append(td.string)
        all_data.append(country)

    data_frame = pandas.DataFrame.from_records(all_data, columns=columns)
    # print(data_frame)
    return data_frame

def fake_data(pd_data):
    num = 60
    s = pd.Series(np.random.randint(1000, 200000, size=244))
    r = {'xxx': s}
    new_data = pd_data.assign(sim_data=s)
    print(new_data)
    new_data.to_csv('country_loc.csv')
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
    pd_data = get_country_info()
    data = fake_data(pd_data)
    print(data)
    gen_heat_map(data)
