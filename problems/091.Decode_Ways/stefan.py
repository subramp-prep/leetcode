# coding=utf-8


class Solution(object):

    def numDecodings(self, s):
        v, w, p = 0, int(s > ''), ''
        for d in s:
            v, w, p = w, (d > '0') * w + (9 < int(p + d) < 27) * v, d
        return w

    def numDecodings(self, s):
        return reduce(lambda(v, w, p), d: (w, (d > '0') * w + (9 < int(p + d) < 27) * v, d), s, (0, s > '', ''))[1] * 1

############ test case ###########
s = Solution()
print s.numDecodings("")
print s.numDecodings("10")
print s.numDecodings("12")

############ comments ############
# 普通的递推
# w tells the number of ways
# v tells the previous number of ways
# d is the current digit
# p is the previous digit
