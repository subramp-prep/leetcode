# coding=utf-8
# Author: Jianghan LI
# Question: Q1
# Complexity: O(N)
# Date: 2017-10-15

import bisect


class Solution(object):

    def fallingSquares(self, positions):
        """
        :type positions: List[List[int]]
        :rtype: List[int]
        """
        height = [0]
        pos = [0]
        res = []
        cur = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            max_height = max(height[i - 1:j] or [0])
            cur = max(cur, max_height + side)
            res.append(cur)
            pos[i:j] = [left, left + side]
            height[i:j] = [max_height + side, height[j - 1]]
        # print zip(pos, height)
        return res

    def fallingSquares(self, positions):
        height = [0]
        pos = [0]
        res = []
        max_h = 0
        for left, side in positions:
            i = bisect.bisect_right(pos, left)
            j = bisect.bisect_left(pos, left + side)
            high = max(height[i - 1:j] or [0]) + side
            pos[i:j] = [left, left + side]
            height[i:j] = [high, height[j - 1]]
            max_h = max(max_h, high)
            res.append(max_h)
        return res


############ test case ###########
s = Solution()
print s.fallingSquares([[100, 100], [200, 100]])  # [100, 100]
print s.fallingSquares([[1, 2], [2, 3], [6, 1]])  # [2, 5, 5]
print s.fallingSquares([[6, 1], [9, 2], [2, 4]])  # [1, 2, 4]
print s.fallingSquares([[2, 1], [2, 9], [1, 8]])  # [1, 10, 18]


############ comments ############
