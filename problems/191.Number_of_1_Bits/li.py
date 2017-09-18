class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = 0
        while n:
            res += 1
            n &= (n-1)
        return res

    def hammingWeight(self, n):
        for i in range(33):
            if not n: return i
            n &= (n - 1)

    # cheat
    def hammingWeight(self, n):
        return bin(n).count('1')


