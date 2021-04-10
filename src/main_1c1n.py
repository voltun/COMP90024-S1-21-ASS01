import json
import os
from afinn_reader import AfinnReader
from grid_parser import GridParser

MELBGRIDFILENAME = "melbGrid.json"
AFINNFILENAME = "AFINN.txt"

def main():
    parent_dir = os.path.dirname(os.path.dirname(__file__))
    twitter_fp = os.path.join(parent_dir, "tinyTwitter.json")

    #Init var
    line_count = 1

    #Init classes
    afinn = AfinnReader(os.path.join(parent_dir, AFINNFILENAME))
    grid = GridParser(MELBGRIDFILENAME)

    print(afinn.calcAFINNScore(["abanDoNs", "abandons.!?", "abandon abandon"]))
    print(grid.getCell(144.85,-37.64))
    #Start looping through all the tweet entries
    with open(twitter_fp,encoding="utf8") as json_file:
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

if __name__ == "__main__":
    main()
