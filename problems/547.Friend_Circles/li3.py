# coding=utf-8
# Author: Jianghan LI
# Question: 547.Friend_Circles
# Complexity: O(N)
# Date: 2018-05 17:16 - 17:18
class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        N = len(M)
        parents = range(N)
        self.count = N
        def add(x):
            if x not in parents:
                parents[x] = x
                self.count += 1
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False

        for i in range(N):
            for j in range(N):
                if M[i][j] == 1:
                    union(i, j)
        return self.count


############ test case ###########
s = Solution()
print s.findCircleNum([[1, 1, 0],
                       [1, 1, 0],
                       [0, 0, 1]])
