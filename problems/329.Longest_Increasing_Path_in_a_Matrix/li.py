# coding=utf-8
# Author: Jianghan LI
# Question: 329.Longest_Increasing_Path_in_a_Matrix
# Date: 2017-05-14 11:17 - 11:47
# Complexity: O(N)


class Solution(object):

    def longestIncreasingPath(self, M):
        """
        :type matrix: List[List[int]]
        :rtype: int
        """
        if not any(M):
            return 0
        d = {}

        def check(i, j):
            if not (i, j) in d:
                d[(i, j)] = max(check(x, y)
                                if 0 <= x < len(M) and 0 <= y < len(M[0]) and M[x][y] > M[i][j] else 0
                                for x, y in [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]) + 1
            return d[(i, j)]
        return max(check(i, j) for i in range(len(M)) for j in range(len(M[0])))


############ test case ###########
s = Solution()
nums = [
    [3, 4, 5],
    [3, 2, 6],
    [2, 2, 1]
]

print s.longestIncreasingPath(nums)

############ comments ############
