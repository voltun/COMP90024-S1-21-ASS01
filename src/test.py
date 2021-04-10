import json
import os

line_count = 1
parent_dir = os.path.dirname(os.path.dirname(__file__))

#Init classes
fp = os.path.join(parent_dir, "tinyTwitter.json")

with open(fp,encoding="utf8") as json_file:
    for line in json_file:
        if line_count == 1:
            total_rows = int(line.split(',')[0].split(':')[1])
            print(total_rows)
        elif line_count >= total_rows:
            json_line = json.loads(line[:-3])
            print(json_line)
        else:
            json_line = json.loads(line[:-2])
            print(json_line)
        line_count += 1
