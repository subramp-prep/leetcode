# coding=utf-8
# Author: Jianghan LI
# Question: 541.Reverse_String_II
# Date: 2017-03-20
# Complexity: O(N)


class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        ret = ''
        i = 0
        flag = 0
        while i < len(s):
            short = s[i:i + k]
            ret += short if flag else short[::-1]
            flag = 1 - flag
            i += k
        return ret


# s[i:i + k][::-1]和s[i + k - 1:i - 1:-1]并不一样
# 因为i=0时，-1是被认作最后一个元素，所以不能用这种写法倒叙到list的开头
