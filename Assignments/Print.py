import json

# 定义文件路径
points_file = r'C:\Users\ASUS\Desktop\mapping_system\Assignment_2\Points.json'
lines_file = r'C:\Users\ASUS\Desktop\mapping_system\Assignment_2\Lines.json'
polygon_file = r'C:\Users\ASUS\Desktop\mapping_system\Assignment_2\Polygon.json'
output_file = r'C:\Users\ASUS\Desktop\mapping_system\Assignment_2\Combined_GeoJSON.json'

# 读取点数据
with open(points_file, 'r') as f:
    point_data = json.load(f)
    if not point_data:
        raise ValueError(f"File {points_file} is empty or not correctly formatted JSON.")

# 读取线数据
with open(lines_file, 'r') as f:
    line_data = json.load(f)
    if not line_data:
        raise ValueError(f"File {lines_file} is empty or not correctly formatted JSON.")

# 读取面数据
with open(polygon_file, 'r') as f:
    polygon_data = json.load(f)
    if not polygon_data:
        raise ValueError(f"File {polygon_file} is empty or not correctly formatted JSON.")

# 合并所有数据
all_data = {
    "type": "FeatureCollection",
    "features": point_data["features"] + line_data["features"] + polygon_data["features"]
}

# 保存为完整的GeoJSON文件
with open(output_file, 'w') as f:
    json.dump(all_data, f, indent=2)

print(f"GeoJSON文件合并完成并保存为 '{output_file}'")
