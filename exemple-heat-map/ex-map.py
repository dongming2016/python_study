#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# author:35037
# datetime:2019/6/1 7:25

import branca
import pandas as pd
import folium
import json
import requests
import webbrowser

url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
county_data = f'{url}/us_county_data.csv'
county_geo = f'{url}/us_counties_20m_topo.json'


df = pd.read_csv(county_data, na_values=[' '])
with open('test.csv', 'wb+') as f:
    f.write(requests.get(county_data).content)

# print(df)

colorscale = branca.colormap.linear.YlOrRd_09.scale(0, 50e3)
employed_series = df.set_index('FIPS_Code')['Employed_2011']
print(employed_series)

def style_function(feature):
    employed = employed_series.get(int(feature['id'][-5:]), None)
    print(employed)
    print('#black' if employed is None else colorscale(employed))
    return {
        'fillOpacity': 0.6,
        'weight': 0,
        'fillColor': '#black' if employed is None else colorscale(employed)
    }


m = folium.Map(
    location=[48, -102],
    tiles='cartodbpositron',
    zoom_start=3
)

folium.TopoJson(
    json.loads(requests.get(county_geo).text),
    'objects.us_counties_20m',
    style_function=style_function
).add_to(m)

file_path = r'heatmap12.html'
m.save(file_path)

webbrowser.open(file_path)

