# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-28


class Solution(object):

  def smallestGoodBase(self, N):
    import math
    n = int(N)
    for k in xrange(int(math.log(n, 2)), 1, -1):
      x = int(n ** k ** -1)  # kth-root of n
      if (1 - x ** (k + 1)) // (1 - x) == n:  # [a^0 + a^1 + ... + a^k] == n
        return str(x)
    return str(n - 1)


# x ^ k < x ^ 0 + x ^ 1 + ... + x ^ k = n <= x ^ (k + 1)
# x ^ (k + 1) - 1 = n * (x - 1)
s = Solution()
print s.smallestGoodBase("7")
print s.smallestGoodBase("4681")
print s.smallestGoodBase("100000000000")


# base最小=位数最多
# 最多位数=math.ceil(math.log(n, 2))
# 根据题意，也可以简化成math.log(n, 2)
# 从这个位数开始，递减试验
