import collections


class Solution(object):

    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while i < j and need[s[i]] < 0:
                    need[s[i]] += 1
                    i += 1
                if not J or j - i <= J - I:
                    I, J = i, j
        return s[I:J]

    # improved by Li
    def minWindow(self, s, t):
        need, missing = collections.Counter(t), len(t)
        i = I = J = 0
        for j, c in enumerate(s, 1):
            missing -= need[c] > 0
            need[c] -= 1
            if not missing:
                while need[s[i]] < 0:  # changed
                    need[s[i]] += 1
                    i += 1
                if not J or j - i < J - I:  # changed
                    I, J = i, j
                missing, need[s[i]], i = 1, need[s[i]] + 1, i + 1  # skip the first char in min-window
        return s[I:J]

############ test case ###########
s = Solution()
print s.minWindow("1SDFFEF21", "12")
