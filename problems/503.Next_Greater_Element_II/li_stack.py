# coding=utf-8
# Author: Jianghan LI
# Question: 503.Next_Greater_Element_II/li_stack.py
# Date: 28/02/2017 23:22


class Solution(object):

    def nextGreaterElements(self, nums):
        stack, res = [], [-1] * len(nums)
        for i in range(len(nums)) * 2:
            while stack and (nums[stack[-1]] < nums[i]):
                res[stack.pop()] = nums[i]
            stack.append(i)
        return res

s = Solution()
print s.nextGreaterElements([1, 2, 1])  # [2,-1,2]
