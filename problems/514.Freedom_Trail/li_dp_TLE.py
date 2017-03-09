# coding=utf-8
# Author: Jianghan LI
# Question: 514.Freedom_Trail
# Date: 08/03/2017 13:55 - 14:21


class Solution(object):

    def findRotateSteps(self, ring, key):
        n = len(ring)
        m = len(key)
        dp = [[0 for i in range(n)] for j in range(m + 1)]
        for i in range(m - 1, -1, -1):
            for j in range(0, n, 1):
                dp[i][j] = float("inf")
                for k in range(0, n, 1):
                    if ring[k] == key[i]:
                        diff = abs(j - k)
                        step = min(diff, n - diff)
                        dp[i][j] = min(dp[i][j], step + dp[i + 1][k])
        return dp[0][0] + m
s = Solution()
print s.findRotateSteps("abcde", "ade")  # 6
print s.findRotateSteps("godding", "godding")  # 13
# print s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")  # 137
