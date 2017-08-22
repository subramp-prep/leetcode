# coding=utf-8
# Author: Jianghan LI
# Question: 506.Relative_Ranks
# Complexity: O(MN)
# Date: 2017-08-09


class Solution(object):

    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not any(matrix):
            return []
        m, n = len(matrix), len(matrix) and len(matrix[0])
        return [matrix[i][j] for i, j in
                sorted([(i, j) for i in range(m) for j in range(n)],
                       key=lambda (i, j): (i + j, (-1, 1)[(i + j) & 1] * i))]

    # 1-line
    def findDiagonalOrder(self, matrix):
        return [matrix[i][j] for i, j in
                sorted([(i, j) for i in range(len(matrix)) for j in range(len(matrix[0]))],
                       key=lambda (i, j): (i + j, (j, i)[(i + j) & 1]))
                ] if any(matrix) else []


############ test case ###########
s = Solution()
print s.findDiagonalOrder([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

############ comments ############
