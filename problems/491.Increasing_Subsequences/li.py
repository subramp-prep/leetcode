# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-21

import itertools


class Solution(object):

  def findSubsequences(self, nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    ret = []
    for i in range(2, len(nums) + 1):
      ret += list(set(itertools.combinations(nums, i)))
    return [x for x in ret if self.isIncreasing(x)]

  def isIncreasing(self, l):
    for i in range(1, len(l)):
      if l[i - 1] > l[i]:
        return False
    return True

############### test cases ###################
s = Solution()
print s.findSubsequences([1, 2, 3, 4])

# brute force 暴力搜索
# 用itertools枚举所有combination
