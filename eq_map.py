import requests
import plotly.express as px
import pandas as pd

eq = requests.get('https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/1.0_month.geojson')
reader_eq = eq.json()

mags, places, lons, lats = [], [], [], []
for eq_dict in reader_eq['features']:
    mag = eq_dict['properties']['mag']
    place = eq_dict['properties']['place']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]

    mags.append(mag)
    places.append(place)
    lons.append(lon)
    lats.append(lat)

data = pd.DataFrame(data=zip(lons, lats, places, mags), columns=['经度', '纬度', '位置', '震级'])

fig = px.scatter(
    data,
    x='经度',
    y='纬度',
    range_x=[-200, 200],
    range_y=[-90, 90],
    width=1600,
    height=800,
    title='全球地震散点图',

    size='震级',
    size_max=10,
    color='震级',
    hover_name='位置',
)

fig.show()
