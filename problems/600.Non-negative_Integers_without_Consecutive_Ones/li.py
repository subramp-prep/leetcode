# coding=utf-8
# Author: Jianghan LI
# Question: /Users/Jianghan/Desktop/test34/600.Non-negative_Integers_without_Consecutive_Ones/li.py
# Date: 2017-05-30
# Complexity: O(N)


class Solution:

    def findIntegers(self, num):
        """
        :type num: int
        :rtype: int
        """
        res = 0
        pre = 0
        fib = lambda n, x=1, y=2: fib(n - 1, y, x + y) if n else x
        n = len(bin(num + 1)[2:])
        for i, v in enumerate(bin(num + 1)[2:]):
            res += fib(n - i - 1) * int(v)
            if pre and int(v):
                break
            pre = int(v)
        return res

    # better
    def findIntegers(self, num):
        x, y = 1, 2
        res = 0
        num += 1
        while num:
            if num & 1 and num & 2:
                res = 0
            res += x * (num & 1)
            num >>= 1
            x, y = y, x + y
        return res

    # better then shorter
    def findIntegers(self, num):
        res, x, y, num = 0, 1, 2, num + 1
        while num:
            res, x, y, num = res if not num & 1 else x if num & 2 else res + x, y, x + y, num >> 1
        return res


############ test case ###########
s = Solution()
for i in range(10):
    print "%2d %5s %2d" % (i, bin(i)[2:], s.findIntegers(i))

############ comments ############
# 转化成二进制考虑。
# 比ox10000小的符合条件的个数是斐波那契数列。
# num & 2 看倒数第二位是否是1
