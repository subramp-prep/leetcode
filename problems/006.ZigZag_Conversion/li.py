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
    interval = numRows * 2 - 1
    rows = [""] * numRows
    rowIndex = 0
    rowOrder = range(numRows) + range(numRows - 2, 0, -1)
    for c in s:
      rows[rowOrder[rowIndex]] += c
      rowIndex = (rowIndex + 1) % len(rowOrder)
    return reduce(lambda x, y: x + y, rows)

########## test case ##########
s = Solution()
print s.convert("PAYPALISHIRING", 3)  # "PAHNAPLSIIGYIR".

# Runtime: 115 ms, O(n), O(n)
# 每一行用一个字符串来记录，最后把每行的字符串reduce一下
# 另一个思路是，直接计算结果，用一个for range(numRows), 每一行的跳跃和是2n-2。应该有不少的性能提升。
# Tags: String
