# coding=utf-8
# Author: Jianghan LI
# Question: 322.Coin_Change
# Complexity: O(N)
# Date: 2017-09-20

import time
from functools import wraps

def timethis(func):
    '''
    Decorator that reports the execution time.
    '''
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        for _ in range(100):
            result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end-start)
        return result
    return wrapper


class Solution(object):

    @timethis
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]

    @timethis
    def coinChange1(self, coins, amount):

        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, amount + 1):
            for c in coins:
                if c <= i:
                    dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]

    @timethis
    def coinChange2(self, coins, amount):
        dp = [float('inf')] * (amount + 1)
        dp[0] = 0
        for c in coins:
            for i in range(c, amount + 1):
                dp[i] = min(dp[i], dp[i - c] + 1)
        return -1 if dp[amount] == float('inf') else dp[amount]

############ test case ###########
import time

s = Solution()
# print s.coinChange([470, 35, 120, 81, 121], 9825)  # 30
s.coinChange([470, 35, 120, 81, 121], 9825)
s.coinChange1([470, 35, 120, 81, 121], 9825)
s.coinChange2([470, 35, 120, 81, 121], 9825)