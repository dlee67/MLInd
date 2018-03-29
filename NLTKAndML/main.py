from WordTagger import WordTagger
import sys

tagger = WordTagger()

def processOptions():
    print(sys.argv[:])
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-lf"):
            tagger.listFunctions()
        if(sys.argv[1] == "-vrb"):
            tagger.verboseModeOn()

if __name__ == "__main__":
  if(len(sys.argv) > 2):
    processOptions()
    tagger.innitFile(sys.argv[2])
    tagger.tokenizeNeedsTagging()
    while(True):

  if(len(sys.argv) == 1):
    tagger.innitFile(sys.argv[1])
    tagger.tokenizeNeedsTagging()
    while(True):
  #tagger.tokenizeNeedsTagging()
  #tagger.toString()
  #tagger.countFrequency("spam")
