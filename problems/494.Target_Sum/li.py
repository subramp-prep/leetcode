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
    count = {0: 1}
    for x in nums:
      count2 = {}
      for tmpSum in count:
        count2[tmpSum + x] = count2.get(tmpSum + x, 0) + count[tmpSum]
        count2[tmpSum - x] = count2.get(tmpSum - x, 0) + count[tmpSum]
      count = count2
    return count.get(S, 0)

  ############### test cases ###################
s = Solution()
print s.findTargetSumWays([1, 1, 1, 1, 1], 3)
print s.findTargetSumWays([0] * 20, 0)

# I used python, but it's really easy to understand.
# To make it clear for everyone,
# find following the syntax for get() method of dictionary(hase map)

# dict.get(key, default)
# The method get() returns a value for the given key.
# If key is not available then returns default value.
