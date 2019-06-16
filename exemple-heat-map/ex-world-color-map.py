import folium
import pandas as pd
import webbrowser

country_geo = 'world-countries.json'

# Setup a folium map at a high-level zoom
map = folium.Map(location=[100, 0], zoom_start=1.5)
data = pd.read_excel('heat.xlsx')
# choropleth maps bind Pandas Data Frames and json geometries.
#This allows us to quickly visualize data combinations
map.choropleth(geo_data=country_geo,
               data=data,
               columns=['CountryCode', 'DT'],
               key_on='properties.name',
               fill_color='YlGnBu', fill_opacity=0.7, line_opacity=0.2)
map.save('test1.html')
webbrowser.open('test1.html')