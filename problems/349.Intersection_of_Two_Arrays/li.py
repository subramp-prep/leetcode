# coding=utf-8
# Author: Jianghan LI
# Question: 349.Intersection_of_Two_Arrays
# Date: 2017-04-03 10:02 - 10:02
# Complexity: O(M+N)


class Solution(object):

    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        return list(set(nums1) & set(nums2))
