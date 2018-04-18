# coding=utf-8
# Author: Jianghan LI
# Question: 697.Degree_of_an_Array
# Complexity: O(N) O(M)
# Date: 2018-04-17


import collections


class Solution(object):

    def findShortestSubArray(self, nums):
        first, counter, res, degree = {}, {}, 0, 0
        for i, v in enumerate(nums):
            first.setdefault(v, i)
            counter[v] = counter.get(v, 0) + 1
            if counter[v] > degree:
                degree = counter[v]
                res = i - first[v] + 1
            elif counter[v] == degree:
                res = min(res, i - first[v])
        return res


############ test case ###########
s = Solution()
print s.findShortestSubArray([1, 2, 2, 3, 1, 4, 2])  # 6
print s.findShortestSubArray([1, 2, 2, 3, 1])  # 2
