# coding=utf-8
# Author: Jianghan LI
# Question: 648.Replace_Words
# Complexity: O(N)
# Date: 2017-09-02 10:23 - 10:27, 1 wrong try


class Solution(object):

    def replaceWords(self, dict, sentence):
        """
        :type dict: List[str]
        :type sentence: str
        :rtype: str
        """
        sentence = sentence.split()
        dict = set(dict)
        for i, w in enumerate(sentence):
            cur = ""
            for c in w:
                cur += c
                if cur in dict:
                    sentence[i] = cur
                    break
        return " ".join(sentence)

# 匹配最短的后，需要break循环
