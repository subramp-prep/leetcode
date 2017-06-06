import re


class WordDictionary:

    def __init__(self):
        self.words = '#'

    def addWord(self, word):
        self.words += word + '#'

    def search(self, word):
        return bool(re.search('#' + word + '#', self.words))
