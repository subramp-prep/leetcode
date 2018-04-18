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
        words = re.sub(r'[^a-zA-Z]', ' ', p).lower().split()
        res = collections.Counter(words).most_common()
        ban = set(banned)
        return iter(w for w, n in res if w not in ban).next()

############ test case ###########
s = Solution()
print s.mostCommonWord("Bob hit a ball, the hit BALL flew far after it was hit.", ["hit"])

############ comments ############
# Edit 1031
# I think it will be more clear if we give real character,
# like paragraph only consists of a-z, A-Z and `!?',;.`
# instead of lowercase, uppercase, space, exclamation mark, question mark, apostrophe, comma, semicolon, and period.


############ explanation ############
# 1. remove all punctuations
# 2. change to lowercase
# 3. words count for each word not in banned set
# 4. return the most common word
