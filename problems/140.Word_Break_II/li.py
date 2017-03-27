# coding=utf-8
# Author: Jianghan LI
# Question: 140.Word_Break_II
# Date: 2017-03-25 22:37 - 11:02


class Solution(object):

    def wordBreak(self, s, wordDict):
        """
        :type s: str
        :type wordDict: List[str]
        :rtype: List[str]
        """
        dp = [0 for _ in range(len(s) + 1)]
        dp[0] = 1
        for i in range(len(s)):
            tmp = s[:i + 1]
            for w in wordDict:
                if tmp.endswith(w):
                    dp[i + 1] += dp[i + 1 - len(w)]
        if dp[-1] == 0:
            return []

        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [[]]
        for i in range(len(s)):
            tmp = s[: i + 1]
            for w in wordDict:
                if tmp.endswith(w):
                    dp[i + 1].extend([l + [w] for l in dp[i + 1 - len(w)]])
        return map(' '.join, dp[-1])

    def wordBreak2(self, s, wordDict):
        dp = [0 for _ in range(len(s))]
        ss = [s[:i + 1] for i in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if ss[i] == w:
                    dp[i] += 1
                elif ss[i].endswith(w):
                    dp[i] += dp[i - len(w)]
        if dp[-1] == 0:
            return []

        dp = [[] for _ in range(len(s))]
        for i in range(len(s)):
            for w in wordDict:
                if ss[i] == w:
                    dp[i].append(w)
                elif ss[i].endswith(w):
                    dp[i].extend([l + " " + w for l in dp[i - len(w)]])
        return dp[-1]

# 第一遍dp
############ test case ###########
s = Solution()
print s.wordBreak2("catsanddog", ["cat", "cats", "and", "sand", "dog"])
