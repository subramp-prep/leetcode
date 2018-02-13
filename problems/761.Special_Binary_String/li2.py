class Solution(object):

    def makeLargestSpecial(self, S):
        def helper(S):
            res = []
            for i in S:
                if i == '1':
                    res.append(helper(S))
                else:
                    return '1' + ''.join(sorted(res)[::-1]) + '0'
            return ''.join(sorted(res)[::-1])
        return helper(iter(S))

    def makeLargestSpecial(self, S):
        S = iter(S)
        res = []
        for i in S:
            if i == '1':
                res.append(self.makeLargestSpecial(S))
            else:
                return '1' + ''.join(sorted(res)[::-1]) + '0'
        return ''.join(sorted(res)[::-1])

    def makeLargestSpecial(self, S):
        res = [[]]
        for i in S:
            if i == '1':
                res.append([])
            else:
                a = '1' + ''.join(sorted(res.pop())[::-1]) + '0'
                res[-1].append(a)
        return ''.join(sorted(res[0])[::-1])


############ test case ###########
s = Solution()
print s.makeLargestSpecial("10")
print s.makeLargestSpecial("11110000")
print s.makeLargestSpecial("1011011000")
