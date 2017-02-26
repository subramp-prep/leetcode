# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-12


class Solution(object):

  def convertTo7(self, num):
    if num < 0:
      return '-' + self.convertTo7(-num)
    elif num < 7:
      return str(num)
    return self.convertTo7(num // 7) + str(num % 7)

s = Solution()
print s.convertTo7(101)
print s.convertTo7(0)

# https://discuss.leetcode.com/topic/79067
