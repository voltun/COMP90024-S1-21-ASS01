from grid_parser import GridParser
import json

GRID = "melbGrid.json"
FILE = "smallTwitter.json"

grid = GridParser(GRID)

with open(FILE,encoding="utf8") as json_file:
    data_list = json.load(json_file)

locationList = []
count = 0
for data in data_list['rows']:
    # temp = data["value"]["geometry"]["coordinates"]
    # words = data["value"]["properties"]["text"].split()
    # textList.append(words)
    # asd = grid.getCell(temp[0], temp[1])
    count += 1
print(count)
