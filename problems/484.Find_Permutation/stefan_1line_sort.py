def findPermutation(self, s):
  return sorted(range(1, len(s) + 2), cmp=lambda i, j: -('I' not in s[j - 1:i - 1]))

# My 1 - liner tells sorted that the(larger) number i comes before
# the(smaller) number j iff they're both under the same D-streak, i.e.,
# iff there's no I between them. (I'm not totally sure that i will always
# be the larger number, but it appears to be the case).
# https://discuss.leetcode.com/topic/
