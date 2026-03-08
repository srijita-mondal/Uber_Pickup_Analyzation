import folium
from sklearn.cluster import KMeans

coords = df[['Lat','Lon']]

kmeans = KMeans(n_clusters=5)
df['cluster'] = kmeans.fit_predict(coords)

map = folium.Map(location=[40.75, -73.98], zoom_start=12)

colors = ['red','blue','green','purple','orange']

for i in range(min(1000, len(df))):
    folium.CircleMarker(
        location=[df.iloc[i]['Lat'], df.iloc[i]['Lon']],
        radius=2,
        color=colors[df.iloc[i]['cluster']]
    ).add_to(map)

map
