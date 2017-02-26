# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-18


class Solution(object):

  def reverse(self, x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
      ret = int(str(x)[::-1])
    else:
      ret = -int(str(-x)[::-1])
    if ret >= math.pow(2, 31) or ret <= -math.pow(2, 31):
    else:
      return ret

########## test case ##########
s = Solution()
print s.reverse(15342364619)
# Runtime: 52ms, O(n)
# 就是偷个懒试一试，高级语言的reverse真是好用。AC的答案思路一样。
