# coding=utf-8
# Author: Jianghan LI
# Question: 537.Complex_Numbe_Multiplication
# Date: 28/03/2017 16:04 - 16:14
# Complexity: O(1)


class Solution(object):

    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = map(int, a[:-1].split('+'))
        b = map(int, b[:-1].split('+'))
        return '%d+%di' % (a[0] * b[0] - a[1] * b[1], a[0] * b[1] + a[1] * b[0])

    def complexNumberMultiply2(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a, ai, b, bi = map(int, (a[:-1] + '+' + b[:-1]).split('+'))
        return '%d+%di' % (a * b - ai * bi, a * bi + ai * b)

s = Solution()
print s.complexNumberMultiply2("1+1i", "1+1i")
