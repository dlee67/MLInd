from WordTagger import WordTagger
import sys

if __name__ == "__main__":
  tagger = WordTagger()
  print("Passed arguments: ", sys.argv[:])
  if(sys.argv[1] == "-lm"):
    tagger.listFunctions()
  tagger.verboseModeOn()
  tagger.innitFile("sometext")
  tagger.tokenizeNeedsTagging()
  #tagger.toString()
  tagger.countFrequency("spam")
