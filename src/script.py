import json
import os
import sys
import time
from afinn_reader import AfinnReader
from grid_parser import GridParser

MELBGRIDFILENAME = "melbGrid.json"
AFINNFILENAME = "AFINN.txt"

# script.py <twitterfilename> <#node> <#core-per-node>
def main(argv):
    #Check input arguments
    if len(argv) < 3:
        print("Insufficient input arguments.\n"+\
        "script.py <twitterfilename> <#node> <#core-per-node>")
        sys.exit(2)

    #Init var
    line_count = 1
    score_dict = {}
    filename = argv[0]
    node = argv[1]
    core_per_node = argv[2]

    #Init classes
    afinn = AfinnReader(AFINNFILENAME)
    grid = GridParser(MELBGRIDFILENAME)


    #Start timer
    start = time.time()
    #Start looping through all the tweet entries
    with open(filename, encoding="utf8") as json_file:
        for line in json_file:
            #Init total number of rows in dataset for tracking
            if line_count == 1:
                total_rows = int(line.split(',')[0].split(':')[1])
                line_count += 1
                continue

            #Iteratively parse a valid JSON, if any. checks the length of line
            #to prevent infinite loop
            while len(line) > 0:
                json_line = is_valid_json(line)

                #If a valid JSON has been parsed, go ahead with processing
                if json_line is not False:
                    break

                #Remove a char from the end of the string that is preventing
                #the string to be a valid JSON format (Could be ',' or parent
                #schema closing tags '}]')
                line = line[:-1]

            #Flag that the the buffer has read to the last line which is not
            #a JSON entry
            if len(line) <= 0:
                break

            line_count += 1

            #Process the tweet
            tweet = ""
            location = []

            tweet = json_line["value"]["properties"]["text"]
            location = json_line["value"]["geometry"]["coordinates"]
            tweet_grid = grid.getCell(location[0], location[1])

            #If the tweet is not from Melbourne, do not continue processing
            if tweet_grid is None:
                continue

            #Calculate the AFINN score of the tweet
            tweet_score = afinn.calcAFINNScore(tweet)

            #Aggregate the score to the appropriate dictionary with grid as
            #the key
            if tweet_grid in score_dict.keys():
                temp = score_dict[tweet_grid]
                score_dict[tweet_grid] = [temp[0] + 1, temp[1] + tweet_score]
            else:
                score_dict[tweet_grid] = []
                score_dict[tweet_grid] = [1, tweet_score]

        #Stop the time elapsed
        end = time.time()

        print("Time elapsed: "+ str((end-start)))
        print_score(score_dict)

#First formats the data then print out the data in an aligned table
#Grid   #Total Tweets   $Overall Sentiment Score
def print_score(score_dict):
    #Print header
    print("Cell".ljust(10)+"#Total Tweets".center(25)+\
        "#Overall Sentiment Score".center(25))
    #Print data
    for grid in score_dict.keys():
        val = score_dict[grid]
        #Formatting + and - signs for score, no signs for 0
        if val[1] < 0:
            score = "-"+str(val[1])
        elif val[1] > 0:
            score = "+"+str(val[1])

        print(grid.ljust(10)+format(val[0],",d").center(25)+score.center(25))

#Returns the JSON dict if the string given is a valid, parsable JSON string,
#returns False otherwise
def is_valid_json(candidate):
    try:
        temp_holder = json.loads(candidate)
    except ValueError as err:
        return False

    return temp_holder

if __name__ == "__main__":
    main(sys.argv[1:])
