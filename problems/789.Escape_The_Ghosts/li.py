# coding=utf-8
# Author: Jianghan LI
# Question: 789.Escape_The_Ghosts
# Complexity: O(N)
# Date: 2018-02-25 0:15:42 - 0:29:45


class Solution(object):

    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]t
        :rtype: bool
        """
        x, y = target
        d = abs(x) + abs(y)
        return all(d < abs(x - i) + abs(y - j) for i, j in ghosts)

############ test case ###########
s = Solution()

ghosts = [[1, 0], [0, 3]]
target = [0, 1]
print s.escapeGhosts(ghosts, target)
# True

ghosts = [[1, 0]]
target = [2, 0]
print s.escapeGhosts(ghosts, target)
# False

ghosts = [[2, 0]]
target = [1, 0]
print s.escapeGhosts(ghosts, target)

############ comments ############
# https://leetcode.com/problems/escape-the-ghosts/discuss/116522/Easy-and-Concise-SolutionC++JavaPython
