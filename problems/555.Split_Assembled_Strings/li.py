# coding=utf-8
# Author: Jianghan LI
# Question: 555.Split_Assembled_Strings
# Date: 2017-04-18 13:55 - 14:16


class Solution(object):

    def splitLoopedString(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        strs = [max(s, s[::-1]) for s in strs]
        res = ""
        for i, s in enumerate(strs):
            for j in range(len(s)):
                words = ''.join(strs[i + 1:] + strs[:i])
                res = max(res, s[j:] + words + s[:j], s[j::-1] + words + s[:j:-1])
        return res
