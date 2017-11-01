# coding=utf-8
# Author: Jianghan LI
# Question: 387.First_Unique_Character_in_a_String
# Complexity: O(N)
# Date: 2017-10-20 10:00 - 10:01


class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        c = collections.Counter(s)
        for i, v in enumerate(s):
            if c[v] == 1:
                return i
        return -1
