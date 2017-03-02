# coding=utf-8
# Author: Jianghan LI
# Question: 451.Sort_Characters_By_Frequency/li.py
# Date: 28/02/2017 00:11-00:19

import collections


class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        c = collections.Counter(s)
        return reduce(lambda a, b: b[1] * b[0] + a, sorted((c[i], i) for i in c), '')

    def frequencySort2(self, s):
        return reduce(lambda a, b: b[1] * b[0] + a, sorted((v, i) for i, v in collections.Counter(s).items()), '')
############ test case ###########
s = Solution()
print s.frequencySort('tree')

############ comments ############
# 计数排序
