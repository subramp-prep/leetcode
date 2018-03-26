# coding=utf-8
# Author: Jianghan LI
# Question: 807.Max_Increase_to_Keep_City_Skyline
# Complexity: O(N)
# Date: 2018-03-24 0:11:06 - 0:20:48, 1 wrong try


class Solution(object):

    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        bot = map(max, grid)
        grid2 = zip(*grid)
        left = map(max, grid2)
        after = 0
        n = len(grid)
        for i in range(n):
            for j in range(n):
                after += min(left[i], bot[j])
        return after - sum(map(sum, grid))

    def maxIncreaseKeepingSkyline(self, grid):
        row, col = map(max, grid), map(max, zip(*grid))
        return sum(min(i, j) for i in row for j in col) - sum(map(sum, grid))

############ test case ###########
s = Solution()
print s.maxIncreaseKeepingSkyline([[3, 0, 8, 4], [2, 4, 5, 7], [9, 2, 6, 3], [0, 3, 1, 0]])  # 35
print s.maxIncreaseKeepingSkyline([[59, 88, 44], [3, 18, 38], [21, 26, 51]])  # 117
