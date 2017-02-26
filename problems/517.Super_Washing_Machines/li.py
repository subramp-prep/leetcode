# coding=utf-8
# Author: Jianghan LI
# Question: 517.Super_Washing_Machines/li.py
# Date: 19/02/2017 22:57-23:20


class Solution(object):

    def findMinMoves(self, machines):
        """
        :type machines: List[int]
        :rtype: int
        """
        if sum(machines) % len(machines) == 0:
            target = sum(machines) / len(machines)
        else:
            return -1
        toLeft = 0
        res = 0
        for i in range(len(machines)):
            toRight = machines[i] - target - toLeft
            res = max(res, toLeft, toRight, toLeft + toRight)
            toLeft = -toRight
        return res

############ test case ###########
s = Solution()
# print s.findMinMoves([1, 0, 5])
# print s.findMinMoves([0, 3, 0])
print s.findMinMoves([9, 1, 8, 8, 9])

############ comments ############
# toLeft: the number of cloths moved to left from this machine
# toRight: the number of cloths moved to right from this machine
# toLeft and toRight may be negative but it's okay.
# https://discuss.leetcode.com/topic/80059
