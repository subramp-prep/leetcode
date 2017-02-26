#!/usr/bin/python
# -*- coding: UTF-8 -*-

from Queue import PriorityQueue as PQueue


class Solution(object):

  def trapRainWater(self, height):
    """
    :type heightMap: List[List[int]]
    :rtype: int
    """
    m = len(height)
    if m == 0:
      return 0
    n = len(height[0])
    if m < 3 or n < 3:
      return 0

    count = [[-1] * n for i in range(m)]
    #count = [[-1 for col in range(n)] for row in range(m)]

    seaList = PQueue()
    for i in range(m):
      count[i][0] = height[i][0]
      count[i][n - 1] = height[i][n - 1]
      seaList.put((height[i][0], i, 0))
      seaList.put((height[i][n - 1], i, n - 1))

    for j in range(1, n - 1):
      count[0][j] = height[0][j]
      count[m - 1][j] = height[m - 1][j]
      seaList.put((height[0][j], 0, j))
      seaList.put((height[m - 1][j], m - 1, j))

    ret = 0
    while not seaList.empty():
      start = seaList.get()
      seaLevel = start[0]
      i = start[1]
      j = start[2]

      if i > 0 and count[i - 1][j] == -1:
        if seaLevel > height[i - 1][j]:
          ret += seaLevel - height[i - 1][j]
          count[i - 1][j] = seaLevel
          seaList.put((seaLevel, i - 1, j))
        else:
          count[i - 1][j] = height[i - 1][j]
          seaList.put((height[i - 1][j], i - 1, j))

      if i < m - 1 and count[i + 1][j] == -1:
        if seaLevel > height[i + 1][j]:
          ret += seaLevel - height[i + 1][j]
          count[i + 1][j] = seaLevel
          seaList.put((seaLevel, i + 1, j))
        else:
          count[i + 1][j] = height[i + 1][j]
          seaList.put((height[i + 1][j], i + 1, j))

      if j > 0 and count[i][j - 1] == -1:
        if seaLevel > height[i][j - 1]:
          ret += seaLevel - height[i][j - 1]
          count[i][j - 1] = seaLevel
          seaList.put((seaLevel, i, j - 1))
        else:
          count[i][j - 1] = height[i][j - 1]
          seaList.put((height[i][j - 1], i, j - 1))

      if j < n - 1 and count[i][j + 1] == -1:
        if seaLevel > height[i][j + 1]:
          ret += seaLevel - height[i][j + 1]
          count[i][j + 1] = seaLevel
          seaList.put((seaLevel, i, j + 1))
        else:
          count[i][j + 1] = height[i][j + 1]
          seaList.put((height[i][j + 1], i, j + 1))

    return ret


s = Solution()
heightMap = [
    [1, 4, 3, 1, 3, 2],
    [3, 2, 1, 3, 2, 4],
    [2, 3, 3, 2, 3, 1]
]
print s.trapRainWater(heightMap)
