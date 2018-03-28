from WordTagger import WordTagger

if __name__ == "__main__":
  tagger = WordTagger()
  tagger.innitFile("sometext")
  tagger.tokenizeNeedTagging()
  tagger.toString()
