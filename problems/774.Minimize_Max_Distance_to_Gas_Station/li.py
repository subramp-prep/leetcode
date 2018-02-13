# coding=utf-8
# Author: Jianghan LI
# Question: 774.Minimize_Max_Distance_to_Gas_Station
# Complexity: O(NlogN)
# Date: 2018-01-28 0:51:19 - 1:00:28, 0 wrong try
import math


class Solution(object):

    def minmaxGasDist(self, st, K):
        """
        :type stations: List[int]
        :type K: int
        :rtype: float
        """
        left, right = 1e-6, st[-1] - st[0]
        while left + 1e-6 < right:
            mid = (left + right) / 2
            count = 0
            for a, b in zip(st, st[1:]):
                count += math.ceil((b - a) / mid) - 1
            if count > K:
                left = mid
            else:
                right = mid
        return right


############ test case ###########
s = Solution()
print s.minmaxGasDist(st=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], K=9)

############ comments ############
