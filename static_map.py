import folium

m = folium.Map(location=[51.9194, 19.1451], zoom_start=7, tiles="CartoDB positron")
m.save("map1.html")
print("saved map1.html")