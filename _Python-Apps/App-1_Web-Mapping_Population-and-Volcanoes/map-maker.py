import folium
map = folium.Map(location=[47.60, -122.33], zoom_start=6, tiles="Stamen Terrain")

fg = folium.FeatureGroup(name="My Map")
fg.add_child(folium.Marker(location=[47.9, -122.7], popup="Hi I am a Marker", icon=folium.Icon(color='green')))

map.add_child(fg)

map.save("Map1.html")