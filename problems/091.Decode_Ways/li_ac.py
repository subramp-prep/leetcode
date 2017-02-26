# coding=utf-8
# Author: Jianghan LI
# Question: 091.Decode_Ways/li.py
# Date: 24/02/2017 00:34


class Solution(object):

    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        dp = [0] * len(s)
        if int(s[0]):
            dp[0] = 1
        else:
            return 0
        if len(s) >= 2 and int(s[1]):
            dp[1] += 1
        if 10 <= int(s[0:2]) <= 26:
            dp[1] += 1
        for i in range(2, len(s)):
            dp[i] = dp[i - 1] * (int(s[i]) > 0) + dp[i - 2] * (10 <= int(s[i - 1:i + 1]) <= 26)
        return dp[-1]

    def numDecodings2(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1] + [0] * len(s)
        for i in range(len(s)):
            dp[i + 1] = dp[i] * (int(s[i]) > 0) + dp[i - 1] * (i and 10 <= int(s[i - 1:i + 1]) <= 26)
        return dp[-1]

    def numDecodings3(self, s):
        if not s or s[0] == '0':
            return 0
        dp = [1] + [0] * len(s)
        for i in range(len(s)):
            dp[i + 1] = dp[i] * (s[i] > '0') + dp[i - 1] * (i and 9 < int(s[i - 1:i + 1]) < 27)
        return dp[-1]

############ test case ###########
s = Solution()
print s.numDecodings("")
print s.numDecodings("10")
print s.numDecodings("12")

############ comments ############
# 普通的递推
