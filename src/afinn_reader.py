import re

class AfinnReader(object):
    afinn_scorelist = []

    #Init class variables
    def __init__(self, filepath):
        with open(filepath, 'r') as f:
            #Converts AFINN words and associated scores into list of lists
            # [..,["word", score],..]
            for line in f:
                self.afinn_scorelist.append(line.split())


    #Takes a list of words and find exact word matches in AFINN.txt, then
    #returns the score of that string.
    def calcAFINNScore(self, sentence):
        score = 0
        #Use regex matching and loop through the entire list of input words
        # with the AFINN words
        for afinn in self.afinn_scorelist:
            for word in sentence:
                if (re.match(r"^("+afinn[0]+")(\.|\?|\!|\'|\"|)*$", word,
                    re.IGNORECASE)):
                    score += int(afinn[1])

        return score
