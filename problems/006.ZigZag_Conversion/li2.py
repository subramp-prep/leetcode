# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-01-18


class Solution(object):

  def convert(self, s, numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    n = numRows
    if n == 1:
      return s
    jumpSum = 2 * n - 2
    ret = ""
    for i in xrange(n):
      jump = 2 * n - 2 - 2 * i
      j = i
      while j < len(s):
        ret += s[j]
        if jump == 0:
          jump = jumpSum
        j += jump
        jump = jumpSum - jump
    return ret

########## test case ##########
s = Solution()
print s.convert("PAYPALISHIRING", 1)  # "PAHNAPLSIIGYIR".

# Runtime: 115 ms, O(n)
# 尼玛打脸，runtime并没什么提高，O(n)的算法里还是常数消耗比较占时间。
# Tags: String
