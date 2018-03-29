# Turns out, read() doesn't return anything.
# https://stackoverflow.com/questions/3211031/python-file-read

import nltk

class WordTagger(object):

    def __init__(self):
        self.isJobCounter = 0
        self.needsTagging = None
        self.afterReading = None
        self.tokens = None
        self.verboseMode = False
        print("WordTagger has been innitialized.")

    def verboseModeOn(self):
        self.verboseMode = True

    def innitFile(self, fileName):
        if(self.verboseMode):
            print("In the block of innitFile.")
        self.needsTagging = open(fileName, "r")
        self.afterReading = self.needsTagging.read()

    def tokenizeNeedsTagging(self):
        if(self.verboseMode):
            print("In the block for tokenizeNeedsTagging.")
        self.tokens = nltk.word_tokenize(self.afterReading)

    def countFrequency(self, findThis):
        fDistObj = nltk.FreqDist(self.tokens)
        if(self.verboseMode):
            print("Consumed:", fDistObj.keys())
        amtOfOccur = fDistObj[findThis]
        #I am guessing the frequency distribution cannot consume anything aside from
        #tokenized string.
        if(self.verboseMode):
            print("The word", findThis, "has occured this much:", amtOfOccur)

    def toString(self):
        print("The needTagging is: ", self.needTagging.read(),
                "\n as a type of: ", type(self.needTagging.read()))
        print("The tokens are: ",  self.tokens,
            "\n as a type of: ", type(self.tokens))
        print("After reading: ", self.afterReading)

    def listFunctions(self):
        print("verboseModeOn <- Each functions prints out the results.\n",
                "innitFile <- Consumes the text file, and prepares it to be tokenized.\n",
                "tokenizeNeedsTagging <- Tokenizes the consumed text file.\n",
                "countFrequency <- Counts the frequency of a certain string token.\n",
                "toString <- prints out all the contents within the fields of WordTagger object, with it's data type.")
