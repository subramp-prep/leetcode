# coding=utf-8
# Author: Jianghan LI
# Question: 307.Range_Sum_Query-Mutable
# Date: 2017-05-15
# Complexity: O(NlogN) O(logN) O(logN)


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        N = len(nums)
        self.l = [0] * (N + 1)
        for i in range(N + 1):
            self.l[i] = sum(nums[i - (i & -i):i])

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.sumRange(i, i)
        i += 1
        while i < len(self.l):
            self.l[i] += diff
            i += i & -i

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        if i:
            return self.sumRange(0, j) - self.sumRange(0, i - 1)
        res = 0
        j = j + 1
        while j:
            res += self.l[j]
            j -= j & -j
        return res


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


############ test case ###########
nums = [1, 3, 4, 5]
c = NumArray(nums)
c.update(0, 2)
c.sumRange(1, 2)


############ comments ############
# __init__ 的复杂度是N * ((logN) / 2 + 1), 递推归纳可求。
# update和sumRange进行位运算，取决于bits个数，复杂度是logN

# http://www.cnblogs.com/zichi/p/4806998.html
# https://zh.wikipedia.org/wiki/%E6%A0%91%E7%8A%B6%E6%95%B0%E7%BB%84
# http://www.hawstein.com/posts/binary-indexed-trees.html
