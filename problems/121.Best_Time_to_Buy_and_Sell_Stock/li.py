# coding=utf-8
# Author: Jianghan LI
# Question: 121.Best_Time_to_Buy_and_Sell_Stock
# Date: 2017-03-26
# Complexity: O(N)


class Solution(object):

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        ret, minp = 0, float('inf')
        for p in prices:
            minp = min(minp, p)
            ret = max(ret, p - minp)
        return ret
