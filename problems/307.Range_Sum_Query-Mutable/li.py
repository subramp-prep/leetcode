# coding=utf-8
# Author: Jianghan LI
# Question: /Users/mac/Work/LeetCode/problems/307.Range_Sum_Query-Mutable/li.py
# Date: 2017-05-11 21:57 - 21:59
# Complexity: O(N)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.l = nums

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        self.l[i] = val

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.l[i:j + 1])


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)
