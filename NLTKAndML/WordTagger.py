import nltk

class WordTagger(object):

    def __init__(self):
        self.needTagging = None
        self.afterReading = None
        self.tokens = None
        print("WordTagger has been innitialized.")

    def innitFile(self, fileName):
        print("In the block of innitFile.")
        self.needTagging = open(fileName, "r")
        self.afterReading = self.needTagging.read()

    def tokenizeNeedTagging(self):
        print("In the block for tokenizeNeedTagging.")
        self.tokens = nltk.word_tokenize(self.afterReading)

    def toString(self):
        print("The needTagging is: ", self.needTagging.read(),
                "\n as a type of: ", type(self.needTagging.read()))
        print("The tokens are: ",  self.tokens,
            "\n as a type of: ", type(self.tokens))
        print("After reading: ", self.afterReading)
