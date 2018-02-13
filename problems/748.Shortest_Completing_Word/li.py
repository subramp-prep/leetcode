# coding=utf-8
# Author: Jianghan LI
# Question: 748.Shortest_Completing_Word
# Complexity: O(N)
# Date: 2017-12-18 0:05:29 - 0:19:42, 0 wrong try


from collections import Counter


class Solution(object):

    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        d = collections.Counter([i.lower() for i in licensePlate if i.isalpha()])
        res = None
        for word in words:
            if (not res or len(word) < len(res)) and all(word.count(
                    c.lower()) + word.count(c.upper()) >= d[c] for c in d):
                res = word
        return res

    def shortestCompletingWord(self, licensePlate, words):
        d = Counter(i.lower() for i in licensePlate if i.isalpha())
        res = None
        for word in words:
            if (not res or len(word) < len(res)) and not d - Counter(word.lower()):
                res = word
        return res

############ test case ###########
s = Solution()
print s.shortestCompletingWord("1s3 456", ["looks", "pest", "stew", "show"])
print s.shortestCompletingWord("1s3 PSt", ["step", "steps", "stripe", "stepple"])

############ comments ############
