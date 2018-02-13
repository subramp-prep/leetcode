# coding=utf-8
# Author: Jianghan LI
# Question: 758.Bold_Words_in_String
# Date: 2018-01-07 0:07:01 - 0:20:05, 0 wrong try


class Solution(object):

    def boldWords(self, words, S):
        """
        :type words: List[str]
        :type S: str
        :rtype: str
        """
        n = len(S)
        isbold = [0] * n
        for i in range(n):
            cur = S[i:]
            for word in words:
                l = len(word)
                if cur.startswith(word):
                    isbold[i:i + l] = [1] * l
        res = []
        cur = 0
        for i, v in enumerate(isbold):
            if cur ^ v:
                if cur:
                    res.append("</b>")
                else:
                    res.append("<b>")
                cur = not cur
            res.append(S[i])
        if cur == 1:
            res.append("</b>")
        return ''.join(res)

############ test case ###########


s = Solution()
words = ["ab", "bc"]
S = "aabcd"
print s.boldWords(words, S)

############ comments ############
