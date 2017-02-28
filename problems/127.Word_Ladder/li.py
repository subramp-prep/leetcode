# coding=utf-8
# Author: Jianghan LI
# Question: 127.Word_Ladder/li.py
# Date: 28/02/2017 13:30 - 14:01


class Solution(object):

    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        wordList = set(wordList)
        dfsList = [beginWord]
        res = 1
        while len(dfsList):
            res += 1
            dfsList2 = []
            for word in dfsList:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        next_word = word[:i] + c + word[i + 1:]
                        if next_word in wordList:
                            if next_word == endWord:
                                return res
                            wordList.remove(next_word)
                            dfsList2.append(next_word)
            dfsList = dfsList2
        return 0

# bfs
