import json
import os

class GridParser:
    grid = []

    def __init__(self, filename):
        parent_dir = os.path.dirname(os.path.dirname(__file__))

        fp = os.path.join(parent_dir, filename)

        with open(fp, encoding="utf8") as json_file:
            data_list = json.load(json_file)

        for data in data_list['features']:
            temp = []
            temp.append(data["properties"]["id"])
            temp.append(data["properties"]["xmin"])
            temp.append(data["properties"]["xmax"])
            temp.append(data["properties"]["ymin"])
            temp.append(data["properties"]["ymax"])
            self.grid.append(temp)
        print(self.grid)

    def getCell(self, lat, long):
        for i in range(len(self.grid)):
            if lat > self.grid[i][1] and lat < self.grid[i][2]\
                and long > self.grid[i][3] and long < self.grid[i][4]:
                return self.grid[i][0]
            if long == self.grid[i][4] and lat >= self.grid[i][1]\
                and lat <= self.grid[i][2]:
                return self.grid[i][0]
        for i in range(len(self.grid)):
            if lat == self.grid[i][2] and long >= self.grid[i][3]\
                and long <= self.grid[i][4]:
                return self.grid[i][0]
            if lat >= self.grid[i][1] and lat <= self.grid[i][2]\
                and long >= self.grid[i][3] and long <= self.grid[i][4]:
                return self.grid[i][0]
