# coding=utf-8
# Author: Jianghan LI
# Question: 093.Restore_IP_Addresses
# Date: 2017-05-13 # 2:22 - 2:34
# Complexity: O(C12^3)


class Solution(object):

    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if len(s) > 12:
            return []

        def check(s):
            return 0 <= int(s) <= 255 and str(int(s)) == s
        res = []
        for i, j, k in itertools.combinations(range(1, len(s)), 3):
            if check(s[:i]) and check(s[i:j]) and check(s[j:k]) and check(s[k:]):
                res.append(s[:i] + "." + s[i:j] + "." + s[j:k] + "." + s[k:])
        return res

# 比如1234567 枚举1<=i<=j<=k<7。
# 检验s[0]-s[i-1].s[j]-s[j-1].s[j]-s[k-1].s[k]-s[6] 是否符合题意
