import json
import os
parent_dir = os.path.dirname(os.path.dirname(__file__))

os.path.join(parent_dir, 'melbGrid.json')

with open(os.path.join(parent_dir, 'melbGrid.json'),encoding="utf8") as json_file:
    data_list = json.load(json_file)

grid = []

for data in data_list['features']:
    temp = []
    temp.append(data["properties"]["id"])
    temp.append(data["properties"]["xmin"])
    temp.append(data["properties"]["xmax"])
    temp.append(data["properties"]["ymin"])
    temp.append(data["properties"]["ymax"])
    grid.append(temp)
print(grid)

def getCell(lat,long):
    for i in range(len(grid)):
        if lat > grid[i][1] and lat < grid[i][2] and long > grid[i][3] and long < grid[i][4]:
            return grid[i][0]
        if long == grid[i][4] and lat >= grid[i][1] and lat <= grid[i][2]:
            return grid[i][0]
    for i in range(len(grid)):
        if lat == grid[i][2] and long >= grid[i][3] and long <= grid[i][4]:
            return grid[i][0]
        if lat >= grid[i][1] and lat <= grid[i][2] and long >= grid[i][3] and long <= grid[i][4]:
            return grid[i][0]


print(getCell(144.85,-37.64))
