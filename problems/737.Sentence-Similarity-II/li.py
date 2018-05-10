# coding=utf-8
# Author: Jianghan LI
# Question: 737.Sentence-Similarity-II
# Complexity: O(N)
# Date: 2018-05 14:50 - 14:56, 1 wrong try

class Solution(object):

    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        parents = {}
        self.count = 0
        def add(x):
            if x not in parents:
                parents[x] = x
                self.count += 1
        def find(x):
            if x not in parents:
                return x
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False
        for x, y in pairs:
            add(x)
            add(y)
            union(x, y)
        if len(words1) != len(words2):
            return False
        for x, y in zip(words1, words2):
            # print find(x), find(y)
            if find(x) != find(y):
                return False
        return True

############ test case ###########
s = Solution()
words1 = ["great", "acting", "skills"]
words2 = ["fine", "drama", "talent"]
pairs = [["great", "good"], ["fine", "good"], ["acting", "drama"], ["skills", "talent"]]
print s.areSentencesSimilarTwo(words1, words2, pairs)


words1 = ["an", "extraordinary", "meal", "meal"]
words2 = ["one", "good", "dinner"]
pairs = [["great", "good"], ["extraordinary", "good"], ["well", "good"], ["wonderful", "good"], ["excellent", "good"], ["fine", "good"], ["nice", "good"], ["any", "one"], ["some", "one"], ["unique", "one"], ["the", "one"], ["an", "one"], ["single", "one"], ["a", "one"], ["truck", "car"], ["wagon", "car"], ["automobile", "car"], ["auto", "car"], ["vehicle", "car"], [
    "entertain", "have"], ["drink", "have"], ["eat", "have"], ["take", "have"], ["fruits", "meal"], ["brunch", "meal"], ["breakfast", "meal"], ["food", "meal"], ["dinner", "meal"], ["super", "meal"], ["lunch", "meal"], ["possess", "own"], ["keep", "own"], ["have", "own"], ["extremely", "very"], ["actually", "very"], ["really", "very"], ["super", "very"]]
print s.areSentencesSimilarTwo(words1, words2, pairs)


############ comments ############
# 1 wrong try for case len(words1) != len(words2)
