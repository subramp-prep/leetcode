# coding=utf-8
# Author: Jianghan LI
# Question: 665.Non-decreasing_Array
# Complexity: O(N)
# Date: 2017-08-27
# Contest47, 00:55:00 - 1:01:00 , 2 wrong tries

class Solution(object):

    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = -1
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                if index >= 0:
                    return False
                else:
                    index = i
        if index == -1 or index == 0 or index == len(nums) - 2:
            return True
        if nums[index - 1] <= nums[index + 1] or nums[index] <= nums[index + 2]:
            return True
        return False

    def checkPossibility(self, nums):
        i = -1
        for j in range(len(nums) - 1):
            if nums[j] > nums[j + 1]:
                if i >= 0:
                    return False
                else:
                    i = j
        if i in [-1, 0, len(nums) - 2]:
            return True
        if nums[i - 1] <= nums[i + 1] or nums[i] <= nums[i + 2]:
            return True
        return False


############ test case ###########
s = Solution()
print s.checkPossibility([3, 4, 2, 3])
