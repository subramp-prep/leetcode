# coding=utf-8
# Author: Jianghan LI
# Question: 623.Add_One_Row_to_Tree
# Date: 2017-06-19 11:20 - 11:25
# Complexity: O(N)


class Solution(object):

    def smallestFactorization(self, a):
        """
        :type a: int
        :rtype: int
        """
        if a < 10:
            return a
        ret = ""
        for i in range(9, 1, -1):
            while a % i == 0:
                ret = str(i) + ret
                a /= i
        return int(ret) if a == 1 and int(ret) < 2**31 else 0


############ test case ###########
s = Solution()
print s.smallestFactorization(48)  # 68
print s.smallestFactorization(1)  # 1
