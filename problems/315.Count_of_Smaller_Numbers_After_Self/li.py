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
############ test case ###########
s = Solution()
# print s.countSmaller([5, 2, 6, 1])
print s.countSmaller([6, 3, 5])

############ comments ############


#
