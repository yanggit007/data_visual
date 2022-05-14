import csv
import json

filename1 = 'data/sitka_weather_2018_simple.csv'
filename2 = 'data/eq_data_30_day_m1.json'

with open(filename1) as f:
    reader_weather = csv.reader(f)
    line_list = next(reader_weather)

    dates, highs, lows = [], [], []
    for row in reader_weather:
        date = row[2]
        high = int(row[5])
        low = int(row[6])

        dates.append(date)
        highs.append(high)
        lows.append(low)

with open(filename2) as f:
    reader_eq = json.load(f)

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
