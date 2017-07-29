# coding=utf-8
# Author: Jianghan LI
# Question: 495.Teemo_Attacking
# Complexity: O(N)
# Date: 2017-07-23 10:10 - 10:14, 0 wrong try


class Solution(object):

    # 总时间－重复时间
    def findPoisonedDuration(self, s, d):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        return len(s) * d - sum(max(0, a + d - b) for a, b in zip(s, s[1:]))

    # 计算sum(min(毒药持续时间, 下次攻击时间－这次攻击时间))
    def findPoisonedDuration(self, s, d):
        return sum(min(d, b - a) for a, b in zip(s, s[1:] + [10e7]))
