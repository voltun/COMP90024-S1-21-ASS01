

def print_score(score_dict):
    #Print header
    # print("%-25s%-25s%-25s" % ("Grid", "#Total Tweets", "#Overall Sentiment Score"))
    # for grid in score_dict.keys():
    #     val = score_dict[grid]
    #     print("%-25s%-25s%-25s" % (grid, str(val[0]), str(val[1])))
    print("Cell".ljust(10)+"#Total Tweets".center(25)+"#Overall Sentiment Score".center(25))
    #Print data
    for grid in score_dict.keys():
        val = score_dict[grid]
        #Formatting + and - signs for score, no signs for 0
        if val[1] < 0:
            score = "-"+str(val[1])
        elif val[1] > 0:
            score = "+"+str(val[1])

        print(grid.ljust(10)+format(val[0],",d").center(25)+score.center(25))



print_score({"C2":[19000,33]})
