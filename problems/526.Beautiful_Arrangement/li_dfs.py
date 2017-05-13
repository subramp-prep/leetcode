class Solution(object):

    def countArrangement(self, N):
        def count(X):
            i = len(X)
            if i == 1:
                return 1
            return sum(count(X - {x}) for x in X if x % i == 0 or i % x == 0)
        return count(set(range(1, N + 1)))

# Improved by stefan solution.
# https://discuss.leetcode.com/topic/79968/easy-python-230ms/7
