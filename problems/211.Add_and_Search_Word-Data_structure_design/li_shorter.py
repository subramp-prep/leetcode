# coding=utf-8
# Author: Jianghan LI
# Question: 211.Add_and_Search_Word-Data_structure_design/li_shorter.py
# Date: 2017-06-02


class WordDictionary(object):

    def __init__(self):
        self.trie = dict()

    def addWord(self, word):
        cur = self.trie
        for c in word + "$":
            cur = cur.setdefault(c, {})

    def search(self, word, cur=None):
        if not cur:
            cur = self.trie
        if not word:
            return "$" in cur
        if 'a' <= word[0] <= 'z':
            return self.search(word[1:], cur[word[0]]) if word[0] in cur else False
        return any(self.search(word[1:], cur[c]) for c in cur if c != "$")

    # shorter
    def search(self, word, cur=None):
        if not cur:
            cur = self.trie
            return "$" in cur if not word \
                else self.search(word[1:], cur[word[0]]) if word[0] in cur \
                else False if 'a' <= word[0] <= 'z' \
                else any(self.search(word[1:], cur[c]) for c in cur if c != "$")
