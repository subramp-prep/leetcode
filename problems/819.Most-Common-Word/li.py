# coding=utf-8
# Author: Jianghan LI
# Question: 1031.Most_Common_Word
# Complexity: O(N)
# Date: 2018-04-12 21:02 - 21:09

import collections
import re
import string


class Solution(object):

    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        words = ''.join(i.lower() if i.isalpha() else ' ' for i in paragraph).split()
        res = collections.Counter(words).most_common()
        ban = set(banned)

        for word, occ in res:
            if word not in ban:
                return word

    def mostCommonWord(self, p, banned):
        ban = set(banned)
        words = re.sub(r'[^a-zA-Z]', ' ', p).lower().split()
        return collections.Counter(w for w in words if w not in ban).most_common(1)[0][0]

############ test case ###########
s = Solution()
print s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])  # ball

############ explanation ############
# 1. remove all punctuations
# 2. change to lowercase
# 3. words count for each word not in banned set
# 4. return the most common word
