import re

class AfinnReader(object):
    afinn_scorelist = []

    #Init class variables
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            #Converts AFINN words and associated scores into list of lists
            # [..,["word", score],..]
            for line in f:
                afinn_scorelist.append(line.split())



    #Takes a list of words and find exact word matches in AFINN.txt, then
    #returns the score of that string.
    def calcAFINNScore(sentence):
        #Use regex and loop through the entire list of input words with the
        #AFINN words
        for afinn in afinn_scorelist:
            for word in sentence:
                if (re.match(r"^("+afinn+")\.\?\!\'\"", re.I))
