
class Solution(object):

    def makeLargestSpecial(self, S):
        def f(*a):
            return '1%s0' % ''.join(sorted(a)[::-1])
        S = S.replace('1', 'f(').replace('0', '),')
        return f(*eval(S))[1:-1]


s = Solution()
print s.makeLargestSpecial("11011000")  # 11100100
print s.makeLargestSpecial("101100")  # 11100100
