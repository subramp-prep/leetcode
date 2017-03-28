class Solution(object):

    def checkPerfectNumber(self, num):
        return (sum([x + (num / x if x * x != num else 0)
                     for x in range(1, int(num ** 0.5) + 1)
                     if num % x == 0]) == 2 * num) if num > 1 else False
