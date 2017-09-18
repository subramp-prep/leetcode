# coding=utf-8
# Author: Jianghan LI
# Question: 661.Image_Smoother
# Complexity: O(MN)
# Date: 2017-08-20
# Contest 46, 0:00:00 - 0:36:46, 6 wrong tries

import math

class Solution(object):

    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        if not any(M):
            return []
        m, n = len(M), len(M[0])
        res = [[0] * n for i in range(m)]
        if m==n==1:
            return M
        if m>1 and n>1:
            for i in range(m):
                for j in range(n):
                    gray = 0
                    if i == 0 and j == 0:
                        gray = M[i][j] + M[i + 1][j] + M[i][j + 1] + M[i + 1][j + 1]
                        res[i][j] = int(math.floor(gray / 4))
                    elif i == 0 and j == n-1:
                        gray = M[i][j] + M[i + 1][j] + M[i][j - 1] + M[i + 1][j - 1]
                        res[i][j] = int(math.floor(gray / 4))
                    elif i == m-1 and j == 0:
                        gray = M[i][j] + M[i - 1][j] + M[i][j + 1] + M[i - 1][j + 1]
                        res[i][j] = int(math.floor(gray / 4))
                    elif i == m-1 and j == n-1:
                        gray = M[i][j] + M[i - 1][j] + M[i][j - 1] + M[i - 1][j - 1]
                        res[i][j] = int(math.floor(gray / 4))
                    elif i == 0:
                        M[i][j - 1] + M[i][j] + M[i][j + 1]
                        gray = M[i][j - 1] + M[i][j] + M[i][j + 1] + \
                            M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]
                        res[i][j] = int(math.floor(gray / 6))
                    elif i == m-1:
                        gray = M[i][j - 1] + M[i][j] + M[i][j + 1] + \
                            M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1]
                        res[i][j] = int(math.floor(gray / 6))
                    elif j == 0:
                        gray = M[i - 1][j] + M[i - 1][j + 1] + \
                            M[i][j] + M[i][j + 1] + \
                            M[i + 1][j] + M[i + 1][j + 1]
                        res[i][j] = int(math.floor(gray / 6))
                    elif j == n-1:
                        gray = M[i - 1][j - 1] + M[i - 1][j] + \
                            M[i][j - 1] + M[i][j] + \
                            M[i + 1][j - 1] + M[i + 1][j]
                        res[i][j] = int(math.floor(gray / 6))
                    else:
                        gray = M[i - 1][j - 1] + M[i - 1][j] + M[i - 1][j + 1] + \
                            M[i][j - 1] + M[i][j] + M[i][j + 1] + \
                            M[i + 1][j - 1] + M[i + 1][j] + M[i + 1][j + 1]
                        res[i][j] = int(math.floor(gray / 9))
        elif m == 1:
            for j in range(n):
                if j == 0:
                    gray = M[0][0] + M[0][1]
                    res[0][0] = int(math.floor(gray / 2))
                elif j == n-1:
                    gray = M[0][n-2] + M[0][n-1]
                    res[0][n-1] = int(math.floor(gray / 2))
                else:
                    gray = M[0][j-1] + M[0][j] +  M[0][j+1]
                    res[0][j] = int(math.floor(gray / 3))

        elif n == 1:
            for i in range(m):
                if i == 0:
                    gray = M[0][0] + M[1][0]
                    res[0][0] = int(math.floor(gray / 2))
                elif i == m-1:
                    gray = M[m-2][0] + M[m-1][0]
                    res[m-1][0] = int(math.floor(gray / 2))
                else:
                    gray = M[i-1][0] + M[i][0] + M[i+1][0]
                    res[i][0] = int(math.floor(gray / 3))
        return res


############ test case ###########
s = Solution()
print s.imageSmoother([
    [1, 1, 1],
    [1, 1, 0],
    [1, 1, 1]]
)
print s.imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
print s.imageSmoother([[6,9,7]])
############ comments ############
