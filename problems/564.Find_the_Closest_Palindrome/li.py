# coding=utf-8
# Author: Jianghan LI
# Question: 564.Find_the_Closest_Palindrome
# Complexity: O(1)
# Date: 2017-09-13

class Solution(object):
    def nearestPalindromic(self, n):
        """
        :type n: str
        :rtype: str
        """
        prefix = int(n[:(len(n)+1)/2])
        res = []
        res.append("9" * ((len(n) - 1) or 1))
        res.append("1" + "0" *  (len(n) - 1) + "1")
        if len(n) & 1:
            res.append(str(prefix) + str(prefix)[-2::-1]),
            res.append(str(prefix-1) + str(prefix-1)[-2::-1])
            res.append(str(prefix+1) + str(prefix+1)[-2::-1])
        else:
            res.append(str(prefix) + str(prefix)[::-1])
            res.append(str(prefix-1) + str(prefix-1)[::-1])
            res.append(str(prefix+1) + str(prefix+1)[::-1])
        res = sorted(map(int, res))
        return str(sorted(res, key=lambda x: abs(int(n)- x) or float('inf'))[0])


# 5种形式
# prefix, prefix+1, prefix+2, 99999, 100001