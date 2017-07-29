# coding=utf-8
# Author: Jianghan LI
# Question: 051.N-Queens
# Complexity: O(N!)
# Date: 2017-07-20 23:47

import itertools


class Solution(object):

    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        res = []
        for c in itertools.permutations(range(n)):
            if len(set(i + v for i, v in enumerate(c))) < n:
                continue
            if len(set(i - v for i, v in enumerate(c))) < n:
                continue
            cur = []
            for v in c:
                cur.append('.' * v + 'Q' + '.' * (n - v - 1))
            res.append(cur)
        return res

    def solveNQueens2(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        return [['.' * v + 'Q' + '.' * (n - v - 1) for v in c]
                for c in itertools.permutations(range(n))
                if (len(set(i + v for i, v in enumerate(c))) == n) and
                (len(set(i - v for i, v in enumerate(c))) == n)]


s = Solution()
print s.solveNQueens(9)

############ comments ############
