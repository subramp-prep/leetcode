# coding=utf-8
# Author: Jianghan LI
# Question: 816.Ambiguous_Coordinates
# Complexity: O(N^3)
# Date: 2018-04-12 21:09 - 21:29

import itertools


class Solution(object):

    def ambiguousCoordinates(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        S = S[1:-1]

        def f(S):
            if not S or len(S) > 1 and S[0] == S[-1] == '0':
                return []
            if S[-1] == '0':
                return [S]
            if S[0] == '0':
                return [S[0] + '.' + S[1:]]
            return [S] + [S[:i] + '.' + S[i:] for i in range(1, len(S))]
        return ['(%s, %s)' % (a, b) for i in range(len(S)) for a, b in itertools.product(f(S[:i]), f(S[i:]))]

############ test case ###########
s = Solution()
print s.ambiguousCoordinates("(123)")
print s.ambiguousCoordinates("(00011)")
print s.ambiguousCoordinates("(0123)")
print s.ambiguousCoordinates("(100)")
print s.ambiguousCoordinates("(0000001)")


############ comments ############
# Edit 1032. Ambiguous Coordinates
# I did one wrong submission for missing the white space between coordinates.
# It will be kind to add a small note maybe.


############ explanation ############
# We split S to two parts as two coordinates.
# Then we use f(S) to find all possible strings for each coordinate.

# In sub functon f(S)
# if S == "":
#     return []
# if S == "0":
#     return [S]
# if S == "0XXX0":
#     return []
# if S == "0XXX":
#     return ["0.XXX"]
# if S == "XXX0":
#     return [S]
# return [S, "X.XXX", "XX.XX", "XXX.X"...]

# Then we add the product of two lists to result.
