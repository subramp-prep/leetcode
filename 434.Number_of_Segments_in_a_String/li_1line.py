# coding=utf-8
# Author: Jianghan LI
# Question: 434.Number_of_Segments_in_a_String/li.py
# Date: 23/02/2017 00:26 - 00:27


class Solution(object):

    def countSegments(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.split())

############ test case ###########
s = Solution()
print s.countSegments("h i")
print s.countSegments("  ")

############ comments ############
