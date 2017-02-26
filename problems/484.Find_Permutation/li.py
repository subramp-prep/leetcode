# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-21


class Solution(object):

  def findPermutation(self, s):
    """
    :type s: str
    :rtype: List[int]
    """
    ret = []
    for i in filter(lambda i: s[i] == 'I', range(len(s))):
      ret.extend(range(i + 1, len(ret), -1))
      print ret
    ret.extend(range(len(s) + 1, len(ret), -1))
    return ret

############### test cases ###################
s = Solution()
print s.findPermutation("DIDDID")


# loop on condition: 循环＋判断条件
# 1.
#   for i in range(len(s)):
#     if s[i] == 'I':
# 2.
#   for i in [i for i in range(len(s)) if s[i] == 'I']:
# 3.
#   for i in filter(lambda i: s[i] == 'I', range(len(s))):

# 贪心法
# I have used a greedy algorithm:
#   1. Loop on the input and insert a decreasing numbers when see a 'I'
#   2. Insert a decreasing numbers to complete the result.
#
# Simple example:
# Input: "DIDDID"
# 0 []
# 1 [2, 1]
# 2 [2, 1]
# 3 [2, 1]
# 4 [2, 1, 5, 4, 3]
# 5 [2, 1, 5, 4, 3]
# [2, 1, 5, 4, 3, 7, 6]

# Then, output is [2, 1, 5, 4, 3, 7, 6]
#
# https://discuss.leetcode.com/topic/76208/python-simple-o-n-solution-in-5-lines/2
