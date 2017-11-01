class Solution(object):

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        res = 1
        k -= 1
        while k > 0:
            count = 0
            left, right = res, res + 1
            while left <= n:
                count += (min(n + 1, right) - left)
                left, right = 10 * left, 10 * right
            if k >= count:
                res += 1
                k -= count
            else:
                res *= 10
                k -= 1
        return res