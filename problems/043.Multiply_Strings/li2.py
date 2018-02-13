# coding=utf-8
# Author: Jianghan LI
# Question: 043.Multiply_Strings
# Complexity: O(M+N)
# Date: 2018-01-08


class Solution(object):

    def multiply(self, num1, num2):
        s1 = [int(i) for i in num1[::-1]]
        s2 = [int(i) for i in num2[::-1]]
        res = [0] * (len(s1) + len(s2))
        for i, a in enumerate(s1):
            for j, b in enumerate(s2):
                res[i + j] += a * b
        carry = 0
        for i in range(len(res)):
            res[i] += carry
            carry = res[i] / 10
            res[i] %= 10
        return ''.join(str(i) for i in res[::-1]).lstrip('0') or '0'


############ test case ###########
s = Solution()
print s.multiply('123', '456')  # 56088
print s.multiply("12", "12")  # 144
print s.multiply("0", "0")  # 0
print s.multiply("9113", "0")  # 0
print s.multiply("99", "9")  # 891


############ test case ###########
s = Solution()  # 880650
