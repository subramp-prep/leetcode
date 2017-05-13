# coding=utf-8
# Author: Jianghan LI
# Question: 315.Count_of_Smaller_Numbers_After_Self
# Date: 2017-05-05 7:34 - 08:29
# Complexity: O(NlogN)


class Solution(object):

    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        def helper(nums):
            n = len(nums)
            if n == 0:
                return ([], nums, [])
            if n == 1:
                return ([0], nums, [0])
            ind1, l1, res1 = helper(nums[:n / 2])
            ind2, l2, res2 = helper(nums[n / 2:])
            ind, l, res = [], [], res1 + res2
            i = j = 0
            while i < n / 2 or j + n / 2 < n:
                if i >= n / 2 or j + n / 2 < n and l1[i] > l2[j]:
                    l.append(l2[j])
                    ind.append(n / 2 + ind2[j])
                    j += 1
                elif j + n / 2 >= n or i < n and l1[i] <= l2[j]:
                    res[ind1[i]] += j
                    l.append(l1[i])
                    ind.append(ind1[i])
                    i += 1
            #print(ind, l, res)
            return (ind, l, res)
        return helper(nums)[2]

    def countSmaller(self, nums):
        def helper(nums):
            n = len(nums)
            if n == 0:
                return ([], [])
            if n == 1:
                return ([0], [0])
            ind1, res1 = helper(nums[:n / 2])
            ind2, res2 = helper(nums[n / 2:])
            # merge, conquer
            ind, res = [], res1 + res2
            i = j = 0
            while i < n / 2 or j + n / 2 < n:
                if i >= n / 2 or j + n / 2 < n and nums[ind1[i]] > nums[n / 2 + ind2[j]]:
                    ind.append(n / 2 + ind2[j])
                    j += 1
                elif j + n / 2 >= n or i < n and nums[ind1[i]] <= nums[n / 2 + ind2[j]]:
                    res[ind1[i]] += j
                    ind.append(ind1[i])
                    i += 1
            return (ind, res)
        return helper(nums)[1]


############ test case ###########
s = Solution()
print s.countSmaller([5, 2, 4, 6, 3, 1])


############ comments ############

# helper返回排序好的数组l，每个数在原数组中的ind，以及本题目要求的结果res。
# 处理收敛情况base case，length等于0或1的情况.

# ind 1 2 0  2 1 0
# l   2 4 5  1 3 6
# res 2 0 0  2 1 0
# m erge=>
# ind 5   1   4   2   0   3
# l   1   2   3   4   5   6
# res 4   1   2   2   1   0

# 根据学生建议，可以删掉排序后的list，只用index查找原数。
