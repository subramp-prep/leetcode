class Solution(object):

    def checkPerfectNumber(self, num):
        def prime_factorization(n):
            d = 2
            while d * d <= n:
                expo = 0
                while n % d == 0:
                    expo += 1
                    n /= d
                if expo:
                    yield d, expo
                d += 1 + (d > 2)
            if n > 1:
                yield n, 1
        divsum = 1
        for p, e in prime_factorization(num):
            divsum *= (p**(e + 1) - 1) / (p - 1)
        return divsum == 2 * num


# https://discuss.leetcode.com/topic/84278/python-straightforward-with-explanation
