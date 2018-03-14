# coding=utf-8
# Author: Jianghan LI
# Question: 799.Champagne_Tower
# Complexity: O(100 * 100)
# Date: 2018-03-10 0:09:07 - 0:37:33, 1 wrong try


class Solution(object):

    def champagneTower(self, poured, query_row, query_glass):
        """
        :type poured: int
        :type query_row: int
        :type query_glass: int
        :rtype: float
        """
        res = [poured] + [0] * 100
        for row in range(1, query_row + 1):
            for i in range(row, 0, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
            res[0] = max(res[0] - 1, 0) / 2.0

        return min(res[query_glass], 1)

    def champagneTower(self, poured, query_row, query_glass):
        res = [poured] + [0] * 100
        for row in range(1, query_row + 1):
            for i in range(row, -1, -1):
                res[i] = max(res[i] - 1, 0) / 2.0 + max(res[i - 1] - 1, 0) / 2.0
        return min(res[query_glass], 1)

############ test case ###########
s = Solution()
print s.champagneTower(poured=4, query_glass=2, query_row=2)  # 0.25
print s.champagneTower(poured=0, query_glass=1, query_row=0)  # 0
print s.champagneTower(poured=1, query_glass=1, query_row=0)  # 0

############ comments ############
# https://leetcode.com/problems/champagne-tower/discuss/118711/O(101)-space-solution-C++Python
