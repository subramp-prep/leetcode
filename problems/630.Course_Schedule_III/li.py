# coding=utf-8
# Author: Jianghan LI
# Question: 629.K_Inverse_Pairs_Array
# Date: 2017-06-27 14:45 - 14:57, 0 wrong try
# Complexity: O(N)

import heapq


class Solution(object):

    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        take = []
        time = 0
        for t, d in sorted(courses, key=lambda x: x[1]):
            time += t
            heapq.heappush(take, (-t, t))
            if time > d:
                time -= heapq.heappop(take)[1]
        return len(take)

    # shorter
    def scheduleCourse(self, courses):
        take, time = [], 0
        for t, d in sorted(courses, key=lambda x: x[1]):
            time += heapq.heappush(take, (-t, t)) or t - (t + time > d and heapq.heappop(take)[1])
        return len(take)

############ test case ###########
s = Solution()
print s.scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]])
