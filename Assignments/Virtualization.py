import folium
import json
from shapely.geometry import shape, Point, LineString, Polygon
import geopandas as gpd

# 加载合并后的GeoJSON数据
with open('C:/Users/ASUS/Desktop/mapping_system/Assignment_2/Combined_GeoJSON.json', 'r', encoding='utf-8') as f:
    combined_geojson = json.load(f)

# 初始化folium地图，中心点设置为纽约市，并设置初始缩放级别
m = folium.Map(location=[40.7128, -74.0060], zoom_start=12)

# 添加地铁路线数据
subway_lines_geojson_path = 'C:/Users/ASUS/Desktop/mapping_system/Assignment_2/subway_lines.geojson'
subway_lines = gpd.read_file(subway_lines_geojson_path)

# 将地铁路线添加到地图
for _, row in subway_lines.iterrows():
    folium.GeoJson(data=row['geometry'].__geo_interface__,
                   style_function=lambda x: {'color': 'blue', 'weight': 2, 'opacity': 0.6}).add_to(m)

# 添加合并后的GeoJSON数据
for feature in combined_geojson['features']:
    geom = shape(feature['geometry'])
    if isinstance(geom, Point):
        folium.Marker([geom.y, geom.x], popup=feature['properties']['name'], icon=folium.Icon(color='green')).add_to(m)
    elif isinstance(geom, LineString):
        folium.GeoJson(data=geom.__geo_interface__,
                       style_function=lambda x: {'color': 'red', 'weight': 2, 'opacity': 0.6}).add_to(m)
    elif isinstance(geom, Polygon):
        folium.GeoJson(data=geom.__geo_interface__,
                       style_function=lambda x: {'color': 'orange', 'weight': 1, 'fillColor': 'orange', 'fillOpacity': 0.4}).add_to(m)

# 保存地图为HTML文件
m.save('C:/Users/ASUS/Desktop/mapping_system/Assignment_2/Daily_Route_Map.html')
