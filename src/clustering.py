import folium

map = folium.Map(location=[40.75, -73.98], zoom_start=12)

for i in range(1000):
    folium.CircleMarker(
        location=[df.iloc[i]['Lat'], df.iloc[i]['Lon']],
        radius=2
    ).add_to(map)

map
