from nltk import nltk

class WordTagger:

    needTagging = None
    tokens = None

    def __init__(self):
        print("WordTagger has been innitialized.")

    def innitFile(self, fileName):
        self.needTagging = open(fileName, "r+")
        print("The contents of needTagging: ", self.needTagging.read())

    def tokenizeNeedTagging(self):
        print("In the block for tokenizeNeedTagging");
        temp = self.needTagging
        tokens = nltk.word_tokenize(temp.read())
        print("tokens are now: ",  tokens)

    def toString(self):
        print("The needTagging is: ", self.needTagging.read())
        print("The tokens are: ",  self.tokens)
