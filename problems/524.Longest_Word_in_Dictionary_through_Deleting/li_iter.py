# coding=utf-8
# Author: Jianghan LI
# Question: 524.Longest_Word_in_Dictionary_through_Deleting
# Date: 10/03/2017


class Solution(object):

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """
        for word in sorted(d, key=lambda w: (-len(w), w)):
            it = iter(s)
            if all(c in it for c in word):
                return word
        return ''
