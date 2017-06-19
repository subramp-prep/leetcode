# coding=utf-8
# Author: Jianghan LI
# Question: 525.Contiguous_Array
# Date: 2017-06-18


class Solution(object):

    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ret, c, d = 0, 0, {0: -1}
        for i, v in enumerate(nums):
            c += (1, -1)[v]
            if c in d:
                ret = max(i - d[c], ret)
            else:
                d[c] = i
        return ret
