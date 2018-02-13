# coding=utf-8
# Author: Jianghan LI
# Question: 761.Special_Binary_String
# Complexity: O(N^2)
# Date: 2018-01-07


class Solution(object):

    def makeLargestSpecial(self, S):
        """
        :type S: str
        :rtype: str
        """
        count = 0
        i = 0
        res = []
        for j, v in enumerate(S):
            if v == '1':
                count += 1
            else:
                count -= 1
            if count == 0:
                res.append(S[i:j + 1])
                i = j + 1
        for i in range(len(res)):
            res[i] = '1' + self.makeLargestSpecial(res[i][1:-1]) + '0'
        return ''.join(sorted(res)[::-1])

    def makeLargestSpecial(self, S):
        count = i = 0
        res = []
        for j, v in enumerate(S):
            count = count + 1 if v == '1' else count - 1
            if count == 0:
                res.append('1' + self.makeLargestSpecial(S[i + 1:j]) + '0')
                i = j + 1
        return ''.join(sorted(res)[::-1])


############ test case ###########
s = Solution()
print s.makeLargestSpecial("11011000")

############ comments ############
