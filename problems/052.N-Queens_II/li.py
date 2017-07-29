# coding=utf-8
# Author: Jianghan LI
# Question: /Users/mac/Work/LeetCode/problems/052.N-Queens_II/li.py
# Complexity: O(N)
# Date: 2017-07-21 09:25


class Solution(object):

    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        return sum(1 for c in itertools.permutations(range(n))
                   if (len(set(i + v for i, v in enumerate(c))) == n) and
                   (len(set(i - v for i, v in enumerate(c))) == n))
