# coding=utf-8
# Author: Jianghan LI
# Question: 402. Remove K Digits
# Date: 2017-03-04 01:01 - 01:17
# Complexity: O(N)


class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return '0'
        stack = []
        for i in num:
            while k and len(stack) and i < stack[-1]:
                stack.pop()
                k -= 1
            stack.append(i)
        res = str(int(''.join(stack)))
        return res[:-k] if k else res
