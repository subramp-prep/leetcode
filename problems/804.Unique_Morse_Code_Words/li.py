# coding=utf-8
# Author: Jianghan LI
# Question: 804.Unique_Morse_Code_Words
# Complexity: O(N)
# Date: 2018-03-24 0:07:08 - 0:11:06, 0 wrong try


class Solution(object):

    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]

        res = set()
        for word in words:
            code = ''.join(d[ord(i) - ord('a')] for i in word)
            res.add(code)
        return len(res)

    def uniqueMorseRepresentations(self, words):
        d = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--",
             "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
        return len({''.join(d[ord(i) - ord('a')] for i in w) for w in words})


############ test case ###########
s = Solution()
print s.uniqueMorseRepresentations(words=["gin", "zen", "gig", "msg"])
