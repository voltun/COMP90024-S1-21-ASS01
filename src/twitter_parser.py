import json

with open('tinyTwitter.json',encoding="utf8") as json_file:
    data_list = json.load(json_file)

textList = []
locationList = []

for data in data_list['rows']:
    words = data["value"]["properties"]["text"].split()
    textList.append(words)
    locationList.append(data["value"]["geometry"]["coordinates"])

print(textList)
print(locationList)
