# coding=utf-8
# Author: Han
# Question: 313. Super Ugly Number
# Date: 2017-03-09
# Complexity: O(N) O(N)


class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [1]
        iprime = [0] * len(primes)
        while len(ugly) < n:
            for i, p in enumerate(primes):
                while ugly[iprime[i]] * p <= ugly[-1]:
                    iprime[i] += 1
            ugly.append(min(ugly[iprime[i]] * p for i, p in enumerate(primes)))
        return ugly[-1]
