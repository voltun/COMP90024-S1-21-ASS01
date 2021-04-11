import json
import os
import time

from afinn_reader import AfinnReader
from grid_parser import GridParser
from mpi4py import MPI

MELBGRIDFILENAME = "melbGrid.json"
AFINNFILENAME = "AFINN.txt"
TWITTERFILENAME = "tinyTwitter.json"

def main():
    # parent_dir = os.path.dirname(os.path.dirname(__file__))
    # twitter_fp = os.path.join(parent_dir, "tinyTwitter.json")

    #Init var
    scoreList = []
    textList = []
    score_dict = {}

    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # get your process ID

    #Init classes
    # afinn = AfinnReader(os.path.join(parent_dir, AFINNFILENAME))
    afinn = AfinnReader(AFINNFILENAME)
    grid = GridParser(MELBGRIDFILENAME)

    # print(afinn.calcAFINNScore(["abanDoNs", "abandons.!?", "abandon abandon"]))
    # print(grid.getCell(144.85,-37.64))

    #Start timer
    start = time.time()
    #The master is the only process that reads the file
    if rank == 0:
        #Start looping through all the tweet entries
        with open(TWITTERFILENAME,encoding="utf8") as json_file:
            data_list = json.load(json_file)

        for data in data_list['rows']:
            text = data["value"]["properties"]["text"]
            location = data["value"]["geometry"]["coordinates"]
            temp = [text,location]
            textList.append(temp)

    # Divide the data among processes
    textList = comm.scatter(textList, root=0)

    for item in textList:
        tweet = item[0]
        location = item[1]
        tweet_grid = grid.getCell(location[0], location[1])

        #If the tweet is not from Melbourne, do not continue processing
        if tweet_grid is None:
            continue

        #Calculate the AFINN score of the tweet
        tweet_score = afinn.calcAFINNScore(tweet)

        #append results to scoreList
        scoreList.append([tweet_grid, tweet_score])

    # Send the results back to the master processes
    results = comm.gather(scoreList,root=0)

    #Aggregate the score to the appropriate dictionary with grid as the key
    for tweet_grid, value in results:
        if tweet_grid in score_dict.keys():
            temp = score_dict[tweet_grid]
            score_dict[tweet_grid] = [temp[0] + 1, temp[1] + tweet_score]
        else:
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


if __name__ == "__main__":
    main()
