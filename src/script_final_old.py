import json
import sys
import numpy
from mpi4py import MPI
from afinn_reader import AfinnReader
from grid_parser import GridParser

MELBGRIDFILENAME = "melbGrid.json"
AFINNFILENAME = "AFINN.txt"

# script_final.py <twitterfilename>
def main(argv):
    #Check input arguments
    if len(argv) < 1:
        print("Insufficient input arguments.\n"+\
        "script.py <twitterfilename>")
        sys.exit(2)

    #Init var
    line_count = 1
    score_dict = {}
    processList = []
    scoreList = []
    filename = argv[0]
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank() # get your process ID
    size = comm.Get_size()

    #Init classes
    afinn = AfinnReader(AFINNFILENAME)
    grid = GridParser(MELBGRIDFILENAME)

    #The master is the only process that reads the file
    if rank == 0:
        textList = []
        #Start looping through all the tweet entries
        with open(filename,encoding="utf8") as json_file:
            data_list = json.load(json_file)

        #Only store [tweet,(x-coord,y-coord)]
        for data in data_list['rows']:
            text = data["value"]["properties"]["text"]
            location = data["value"]["geometry"]["coordinates"]
            temp = [text,location]
            textList.append(temp)

        #Splice the entire list into number of list == number of cores
        processList = numpy.array_split(textList, size)

    # Divide the data among processes
    dataList = comm.scatter(processList, root=0)

    #Process the tweets
    for item in dataList:
        tweet = item[0]
        location = item[1]
        tweet_grid = grid.getCell(location[0], location[1])

        #If the tweet is not from Melbourne, do not continue processing
        if tweet_grid is None:
            continue

        #Calculate the AFINN score of the tweet
        tweet_score = afinn.calcAFINNScore(tweet)

        #append results to scoreList
        scoreList.append({tweet_grid: tweet_score})

    # Send the results back to the master process
    results = comm.gather(scoreList, root=0)

    # Master process compiles all the results and print output
    if comm.rank == 0:
        master_dict = {}

        #Compile processed data from all the cores
        for dict_list in results:
            for data in dict_list:
                for i in data.keys():
                    grid_key = i
                    break

                #Continuous dict updates
                if grid_key in master_dict.keys():
                    temp = master_dict[grid_key]
                    master_dict[grid_key] = [temp[0] + 1, temp[1] + \
                        data[grid_key]]
                else:
                    master_dict[grid_key] = []
                    master_dict[grid_key] = [1, data[grid_key]]

        print_score(master_dict)
    else:
        results = None


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
    main(sys.argv[1:])
