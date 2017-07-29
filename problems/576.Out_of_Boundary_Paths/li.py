# coding=utf-8
# Author: Jianghan LI
# Question: 576.Out_of_Boundary_Paths
# Complexity: O(N)
# Date:  2017-07-29 12:08 - 12:25, 2 wrong try


class Solution(object):

    def findPaths(self, m, n, N, i, j):
        """
        :type m: int
        :type n: int
        :type N: int
        :type i: int
        :type j: int
        :rtype: int
        """
        M = [[0 for x in range(n)] for y in range(m)]
        M[i][j] = 1
        ret = 0
        for _ in range(N):
            ret += sum(M[i][0] + M[i][n - 1] for i in range(m)) \
                + sum(M[0][j] + M[m - 1][j] for j in range(n))
            M = [[(i and M[i - 1][j]) + (i + 1 < m and M[i + 1][j])
                  + (j and M[i][j - 1]) + (j + 1 < n and M[i][j + 1])
                  for j in range(n)] for i in range(m)]
        return ret % (10**9 + 7)

    def findPaths(self, m, n, N, x, y):
        M = [[0 for i in range(n)] for j in range(m)]
        for _ in range(N):
            M = [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                  + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                  for j in range(n)] for i in range(m)]
        return M[x][y] % (10 ** 9 + 7)

    def findPaths(self, m, n, N, x, y):
        return reduce(lambda M, _:
                      [[(i == 0 or M[i - 1][j]) + (i + 1 == m or M[i + 1][j])
                        + (j == 0 or M[i][j - 1]) + (j + 1 == n or M[i][j + 1])
                          for j in range(n)] for i in range(m)], range(N),
                      [[0 for i in range(n)] for j in range(m)])[x][y] % (10 ** 9 + 7)
# Wrong try: M初始化不能用i，j。否则会覆盖i，j的输入值。
# Wrong try: 不要忘记mod
