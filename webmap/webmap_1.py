import folium
print(dir(folium))
# create a map object
map = folium.Map(location=[40.897934, -73.885948], zoom_start = 7)
print(map)
#need html file out of this object - to create a map
#look in the Map method directory to see all the methods we can apply to MAP

print(dir(folium.Map))
print(map.save('test.html'))
# go look under your files for the surprise
#rt click on html file and open in browser

#change zoom to 15 and add tiles  = 'Stamen Terrain'  and recreate the html file

map2 = folium.Map(location= [40.897934, -73.885948], zoom_start = 15, tiles = 'Stamen Terrain')
print(map2)
print(map2.save('test2.html'))