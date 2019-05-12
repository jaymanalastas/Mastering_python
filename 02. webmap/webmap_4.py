# we can integrate some if statements to make the cloud color change based on elevation

import folium
import pandas as pd


map4 = folium.Map(location = [40.897934, -73.885948], zoom_start = 15, tiles = 'Stamen Terrain')
df = pd.read_csv('Volcanoes.txt')

# we need to add elev. to our loops as an indicator

for lat,lon,name,elev in zip(df['LAT'], df['LON'], df['NAME'], df['ELEV']):
#we want to say if elev. is at x elevation make color y
# the problem is our expression (color) is inside a method, we can use an inline statment

    folium.Marker(location=[lat,lon], popup = name, icon = folium.Icon(color = 'green' if elev in range (0,1000) else 'orange' if elev in range(1001,1999) else 'blue' if elev in range(2000,2999) else 'red', icon = 'cloud')).add_to(map4)

print(map4.save('test5.html'))