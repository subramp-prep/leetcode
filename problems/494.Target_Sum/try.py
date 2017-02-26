# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-21


class Solution(object):

  def findTargetSumWays(self, nums, S):
    """
    :type nums: List[int]
    :type S: int
    :rtype: int
    """
    if len(nums) == 0:
      return int(S == 0)
    else:
      return self.findTargetSumWays(nums[1::], S + nums[0]) + self.findTargetSumWays(nums[1::], S - nums[0])

  ############### test cases ###################
s = Solution()
print s.findTargetSumWays([1, 1, 1, 1, 1], 3)
print s.findTargetSumWays([0] * 20, 0)

# dp，但是复杂度还是exp的，因为字典的长度是exp的
# 但是题目限制了input的长度，所以暴力搜索结果应该差不多
# 因为不是尾递归，效率其实不太好，c＋＋就过了，python就不过
