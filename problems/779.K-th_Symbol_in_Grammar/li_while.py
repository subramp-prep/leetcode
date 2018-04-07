class Solution(object):

    def kthGrammar(self, N, K):
        res = 0
        while K > 1:
            K = K + 1 if K % 2 else K / 2
            res ^= 1
        return res


if K % 2 == 1, it is the first number in '01' or '10',
if Kth number is 0, K + 1 th is 1.
if Kth number is 1, K + 1 th is 0.
so it will be different from K + 1.

if K % 2 == 0, it is the second number in '01' or '10', generated from K / 2 th number.
if Kth number is 0, it is generated from 1.
if Kth number is 1, it is generated from 0.
