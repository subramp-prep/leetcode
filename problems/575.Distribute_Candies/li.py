# coding=utf-8
# Author: Jianghan LI
# Question: 575.Distribute_Candies
# Date: 2017-06-12 09:34 - 09:34
# Complexity: O(N)


class Solution(object):

    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        return min(len(candies) / 2, len(collections.Counter(candies)))

# 返回min(candies数量一半,candies种类个数)
