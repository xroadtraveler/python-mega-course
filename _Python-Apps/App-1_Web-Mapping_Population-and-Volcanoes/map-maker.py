import pandas
import folium


# This section extracts latitude and longitude from 'Volcanoes.csv'
data = pandas.read_csv("Volcanoes.csv")
lat = list(data["LAT"])
lon = list(data["LON"])


# This section creates our initial map object
map = folium.Map(location=[47.60, -122.33], zoom_start=6, tiles="Stamen Terrain")


# This line creates a single feature group to input all the children into our map
fg = folium.FeatureGroup(name="My Map")


# This section iterates over coordinates to add Marker Points to map
for lt, ln in zip(lat, lon):
    fg.add_child(folium.Marker(location=[lt, ln], popup="Hi I am a Marker", icon=folium.Icon(color='green')))


# This line adds the whole feature group at once
map.add_child(fg)

map.save("Map1.html")