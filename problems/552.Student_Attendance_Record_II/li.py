# coding=utf-8
# Author: Jianghan LI
# Question: 552.Student_Attendance_Record_II
# Date: 2017-04-16 8:11 - 8:33
# Complexity: O(N)


class Solution(object):

    def checkRecord(self, n):
        mod = 10 ** 9 + 7
        if n == 0:
            return 0
        if n == 1:
            return 3
        A = 3  # AP, PA, LA
        O = 2  # PP,LP
        AL = 1  # AL
        LL = 1  # LL
        L = 1  # PL
        ALL = 0
        for i in range(n - 2):
            A, O, AL, LL, L, ALL = sum((A, O, AL, LL, L, ALL)) % mod, sum((O, L, LL)) % mod, A, L, O, AL
        return sum((A, O, AL, LL, L, ALL)) % mod

    def checkRecord2(self, n):
        mod = 10 ** 9 + 7
        O = 1
        A = AL = ALL = L = LL = 0
        for i in range(n):
            # print "%3d %3d %3d %3d %3d %3d" % (A, O, AL, ALL, L, LL)
            A, O, AL, ALL, L, LL = sum((A, O, AL, LL, L, ALL)), sum((O, L, LL)), A, AL, O, L
        # print "%3d %3d %3d %3d %3d %3d" % (A, O, AL, ALL, L, LL)
        return sum((A, O, AL, LL, L, ALL))

    def checkRecord3(self, n):
        n += 1
        a = (1 + 5**0.5) / 4
        b = (1 - 5**0.5) / 4
        res = 2**n / 5**0.5 * ((1 - a**n) / (1 - a) * a - (1 - b**n) / (1 - b) * b)
        return int(res)

s = Solution()
print s.checkRecord2(2)
# print s.checkRecord3(5)

####
# checkRecord3是求得通项公式，公式对的，但是float准确度很不够
