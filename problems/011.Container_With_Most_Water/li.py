# coding=utf-8
# Author: Jianghan LI
# Question: 011.Container_With_Most_Water
# Complexity: O(N)
# Date: 2017-04-23 23:07 - 23:17


class Solution(object):

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[l] > height[r]:
                r -= 1
            else:
                l += 1
                r -= 1
        return res

    def maxArea2(self, height):
        res, l, r = 0, 0, len(height) - 1
        while l < r:
            h = min(height[l], height[r])
            res, l, r = max(res,  h * (r - l)), l + height[l] == h, r - height[r] == h
        return res
