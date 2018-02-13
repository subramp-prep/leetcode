# coding=utf-8
# Author: Jianghan LI
# Question: 457.Circular_Array_Loop
# Complexity: O(N)
# Date: 2018-01-09


class Solution(object):

    # O(N^2), O(1)
    def circularArrayLoop(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        n = len(nums)
        for i in range(n):
            forward = nums[i] > 0
            cur = (nums[i] + i) % n
            while cur != i and (nums[cur] > 0) is forward and nums[cur] % n:
                cur = (nums[cur] + cur) % n
            if cur == i and nums[cur] % n:
                return True
        return False

    # O(N), O(1)
    def circularArrayLoop(self, nums):
        n = len(nums)
        for i in range(n):
            if not nums[i]:
                continue
            forward = nums[i] > 0
            cur = (nums[i] + i) % n
            while cur != i and (nums[cur] > 0) is forward and nums[cur] % n:
                cur = (nums[cur] + cur) % n
            if cur == i and nums[cur] % n:
                return True
            while i != cur and nums[i] % n:
                nums[i], i = 0, (nums[i] + i) % n
        return False

############ test case ###########
s = Solution()
# print s.circularArrayLoop([-1, 2]) #False
print s.circularArrayLoop([-2, 1, -1, -2, -2])  # False

############ comments ############
# Solution1 暴力寻找
# Solution2 遍历过的赋值为1
