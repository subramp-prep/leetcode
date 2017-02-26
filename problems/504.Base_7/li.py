# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-12 03:30


class Solution(object):

  def convertTo7(self, num):
    """
    :type num: int
    :rtype: str
    """
    if num == 0:
      return '0'
    n = abs(num)
    res = ''
    while n:
      res = str(n % 7) + res
      n //= 7
    return res if num >= 0 else '-' + res

s = Solution()
print s.convertTo7(101)
