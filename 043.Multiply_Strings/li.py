# coding=utf-8
# Author: Jianghan LI
# Question: 043.Multiply_Strings/li.py
# Date: 20/02/2017 01:01-01:22


class Solution(object):

    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        res = [0] * (len(num1) + len(num2))
        num1 = map(int, list(num1))[::-1]
        num2 = map(int, list(num2))[::-1]
        print num1, num2
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i + j] += num1[i] * num2[j]
        print res
        carry = 0
        for i in range(len(res)):
            res[i] += carry
            carry = res[i] // 10
            res[i] %= 10
        print res
        res = ''.join(map(str, res[::-1]))
        return str(int(''.join(map(str, res[::-1]))))

############ test case ###########
s = Solution()
print s.multiply('123', '456')

############ comments ############
