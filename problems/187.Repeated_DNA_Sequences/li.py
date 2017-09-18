# coding=utf-8
# Author: Jianghan LI
# Question: 187.Repeated_DNA_Sequences
# Complexity: O(N)
# Date: 2017-08-25 11:05 - 11:


class Solution(object):

    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        cur = s[:10]
        d = {cur: 1}
        for i in s[10:]:
            cur = (cur + i)[1:]
            d[cur] = d.get(cur, 0) + 1
        return [s for s in d if d[s] > 1]

    def findRepeatedDnaSequences(self, s):
        d = collections.Counter(s[i: i + 10] for i in range(len(s) - 9))
        return [s for s in d if d[s] > 1]



