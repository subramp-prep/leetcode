# coding=utf-8
# Author: Jianghan LI
# Question: 371.Sum_of_Two_Integers
# Complexity: O(N)
# Date: 2017-08-14


class Solution(object):

    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        return sum([a, b])

    def getSum(self, a, b):
        while b != 0:
            a, b = (a ^ b) & 0xFFFFFFFF, ((a & b) << 1) & 0xFFFFFFFF
        return a | (~0xFFFFFFFF) if a & 0x80000000 else a

    def getSum(self, a, b):
        def add(a, b):
            if not a or not b:
                return a or b
            return add(a ^ b, (a & b) << 1)

        if a * b < 0:  # assume a < 0, b > 0
            if a > 0:
                return self.getSum(b, a)
            if -a == b:
                return 0
            if -a < b:
                return -add(-a, -b)

        return add(a, b)

############ test case ###########
s = Solution()
print s.getSum(-1, 2)
print s.getSum(-1, -1)

############ comments ############
