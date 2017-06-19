# coding=utf-8
# Author: Jianghan LI
# Question: 621.Task_Scheduler
# Date: 2017-06-19 13:39 - 13:50, 0 wrong try
# Complexity: O(N)

import collections


class Solution(object):

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        c = collections.Counter(tasks)
        maxt = max(c[i] for i in c)
        a = (maxt - 1) * (n + 1) + sum(c[i] == maxt for i in c)
        return max(len(tasks), a)

    def leastInterval(self, tasks, n):
        c = collections.Counter(tasks).values()
        return max(len(tasks), (max(c) - 1) * (n + 1) + counts.count(max(c)))


############ test case ###########
s = Solution()
print s.leastInterval(['A', 'A', 'A', 'B', 'B', 'B'], 2)
