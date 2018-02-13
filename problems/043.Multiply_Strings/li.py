# coding=utf-8
# Author: Jianghan LI
# Question: 043.Multiply_Strings/li.py
# Date: 2017-02-20 01:01-01:22


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        num1 = map(int, num1)[::-1]
        num2 = map(int, num2)[::-1]
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += num1[i] * num2[j]
        carry = 0
        for i in range(len(res)):
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
        return str(int(''.join(map(str, res[::-1]))))

############ test case ###########
s = Solution()
print s.multiply('123', '456')  # 880650
print s.multiply('0', '0')  # 880650

############ comments ############
