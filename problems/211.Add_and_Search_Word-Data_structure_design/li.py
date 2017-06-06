# coding=utf-8
# Author: Jianghan LI
# Question: /Users/Jianghan/MyWork/LeetCode/problems/211.Add_and_Search_Word-Data_structure_design/li.py
# Date: 2017-06-02 11:00 - 11:25


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = dict()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        cur = self.trie
        for c in word + "$":
            cur = cur.setdefault(c, {})

    def search(self, word, cur=None):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        if not cur:
            cur = self.trie
        if word:
            if 'a' <= word[0] <= 'z':
                if word[0] in cur:
                    return self.search(word[1:], cur[word[0]])
                else:
                    return False
            else:
                return any(self.search(word[1:], cur[chr(97 + i)]) for i in range(26) if chr(97 + i) in cur)
        else:
            return "$" in cur

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
