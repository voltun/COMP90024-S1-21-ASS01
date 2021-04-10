import re

class AfinnReader(object):
    afinn_scorelist = []

    #Init class variables
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            #Converts AFINN words and associated scores into list of lists
            # [..,["word", score],..]
            for line in f:
                split_line = line.split()
                self.afinn_scorelist.append(["".join(split_line[:-1]),\
                    split_line[-1]])


    #Takes a sentence as string and find all exact word matches in AFINN.txt as
    #per the project specifications, then returns the score of that string.
    def calcAFINNScore(self, sentence):
        score = 0
        #Use regex matching and loop through the entire list of input words
        # with the AFINN words
        for afinn in self.afinn_scorelist:
            found_list = []
            found_list = re.findall(r"((\s+|^)"+afinn[0]+ \
            "(\s+|$))|((\s+|^)"+afinn[0]+"(\.|\,|\?|\!|\'|\")+)", sentence, \
                re.IGNORECASE)
                
            #Increment total score by number of exact match occurences, if any
            if (len(found_list) > 0):
                score += int(afinn[1]) * len(found_list)

        return score
