# coding=utf-8
# Author: Jianghan LI
# Question: 560.Subarray_Sum_Equals_K
# Date: 2017-05-02

import collections


class Solution(object):

    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count, cur, res = {0: 1}, 0, 0
        for v in nums:
            cur += v
            res += count.get(cur - k, 0)
            count[cur] = count.get(cur, 0) + 1
        return res

    def subarraySum(self, nums, K):
        count, cur, res = collections.Counter([0]), 0, 0
        for v in nums:
            cur += v
            res += count[cur - k]
            count[cur] += 1
        return res
