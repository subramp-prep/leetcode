class Solution(object):

    def minWindow(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """
        # dp[c][i], represent next occurrence index of char c after index i
        N = len(S)
        dp = {c: [N * 2] * N for c in set(T)}
        for c in dp:
            for i in range(N - 1)[::-1]:
                dp[c][i] = i + 1 if S[i + 1] == c else dp[c][i + 1]
        res = S + "#"
        for i in range(N):
            if S[i] == T[0]:
                cur = i
                for c in T[1:]:
                    if cur < N:
                        cur = dp[c][cur]
                if cur - i + 1 < len(res):
                    res = S[i:cur + 1]
        return res if len(res) <= N else ""


############ test case ###########
s = Solution()
print s.minWindow(S="abcdebdde", T="bde")


############ comments ############
# Prepare dp, O(S)
# dp[c][i], represent next occurrence index of char c after index i

# Try every possiblity, O(ST)
# For every char c in S:
#   if c == T[0], start search
#       for every char in T:
#           get next occurence index from dp
