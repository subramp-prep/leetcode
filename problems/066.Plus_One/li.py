# coding=utf-8
# Author: Jianghan LI
# Question: 066.Plus_One
# Complexity: O(N)
# Date: 2017-08-02 10:51-10:53, 0 wrong try


class Solution(object):

    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[-1 - i] < 9:
                return digits[:-1 - i] + [digits[-1 - i] + 1] + [0] * i
        return [1] + [0] * len(0)

    def plusOne(self, digits):
        for i in range(len(digits)):
            if digits[-1 - i] < 9:
                digits[-1 - i] += 1
                return digits
            digits[-1 - i] = 0
        return [1] + digits


def plusOne(self, digits):
    return (digits[:-1] + [digits[-1] + 1] if digits[-1] < 9 else self.plusOne(digits[:-1]) + [0]) if digits else [1]
