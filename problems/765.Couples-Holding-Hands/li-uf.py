# coding=utf-8
# Author: Jianghan LI
# Question: 765.Couples-Holding-Hands
# Complexity: O(N)
# Date: 2018-05-08
class Solution(object):

    def minSwapsCouples(self, row):
        n = len(row)
        parents = {i: i for i in range(n)}
        self.count = n
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

        for i in range(0, len(row), 2):
            union(row[i], row[i + 1])
            union(i, i + 1)
        return n / 2 - self.count

############ test case ###########
s = Solution()
# print s.minSwapsCouples([0, 2, 1, 3])  # 1
# print s.minSwapsCouples([3, 2, 0, 1])  # 0
print s.minSwapsCouples([6, 2, 1, 7, 4, 5, 3, 8, 0, 9])  # 3
