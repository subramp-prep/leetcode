# -*- coding: utf-8 -*
# Author:      Jianghan LI
# File:        li.py
# Create Date: 2017-02-05 11:09-11:16


class Solution(object):

  def findDiagonalOrder(self, matrix):
    """
    :type matrix: List[List[int]]
    :rtype: List[int]
    """
    if len(matrix) == 0:
      return []
    M, N = len(matrix), len(matrix[0])
    if M == 1:
      return matrix[0]
    if N == 1:
      return reduce(lambda a, b: a + b, matrix)
    ret = []
    for i in range(M + N):
      if i % 2 == 1:
        for j in range(i + 1):
          if j >= M or i - j >= N:
            continue
          ret.append(matrix[j][i - j])
      else:
        for j in range(i + 1):
          if i - j >= M or j >= N:
            continue
          ret.append(matrix[i - j][j])
    return ret


s = Solution()
print s.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
