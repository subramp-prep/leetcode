# coding=utf-8
# Author: Jianghan LI
# Question: /Users/mac/Work/LeetCode/problems/274.H-Index/li.py
# Date: 2017-05-23 9:12-9:27
# Complexity: O(NlogN)


class Solution(object):

    def hIndex(self, cita):
        return max(i + 1 for i, v in enumerate(sorted(cita, reverse=True)) if i + 1 <= v) if any(cita) else 0
