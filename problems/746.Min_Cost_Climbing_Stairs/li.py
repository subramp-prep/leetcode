# coding=utf-8
# Author: Jianghan LI
# Question: 746.Min_Cost_Climbing_Stairs
# Complexity: O(N)
# Date: 2017-12-17 0:00:00 - 0:05:29, 0 wrong try


class Solution(object):

    def minCostClimbingStairs(self, cost):
        """
        :type cost: List[int]
        :rtype: int
        """
        for i in range(2, len(cost)):
            cost[i] += min(cost[i - 1], cost[i - 2])
        return min(cost[-2:])


############ test case ###########
s = Solution()
print s.minCostClimbingStairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1])  # 6
print s.minCostClimbingStairs([10, 15, 20])  # 15
print s.minCostClimbingStairs([10, 15])  # 10
