# coding=utf-8
# Author: Jianghan LI
# Question: 299.Bulls_and_Cows
# Date: 2017-06-16 9:12-9:19


class Solution(object):

    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        A = sum(a == b for a, b in zip(secret, guess))
        B = collections.Counter(secret) & collections.Counter(guess)
        return "%dA%dB" % (A, sum(B.values()) - A)
