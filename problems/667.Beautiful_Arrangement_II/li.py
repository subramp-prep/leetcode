# coding=utf-8
# Author: Jianghan LI
# Question: 667.Beautiful_Arrangement_II
# Complexity: O(N)
# Date: 2017-08-27
# Contest47, 01:18:02 - 1:28:29 , 1 wrong try


class Solution(object):

    def constructArray(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[int]
        """
        if k > n - 1:
            return False
        l = 2
        r = n
        res = [1]
        while k > 1:
            if len(res) & 1:
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
            k -= 1
        if len(res) & 1:
            res.extend(range(l, r + 1))
        else:
            res.extend(range(r, l - 1, -1))
        return res

    def constructArray(self, n, k):
        l, r, res = 2, n, [1]
        for _ in range(k - 1):
            if len(res) & 1:
                res.append(r)
                r -= 1
            else:
                res.append(l)
                l += 1
        return res + (range(l, r + 1) if len(res) & 1 else range(r, l - 1, -1))


############ test case ###########
s = Solution()
print s.constructArray(3, 2)
print s.constructArray(5, 2)
