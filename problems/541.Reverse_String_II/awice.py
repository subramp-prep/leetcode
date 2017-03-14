class Solution(object):

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in xrange(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return "".join(s)


# https://discuss.leetcode.com/topic/82596/python-straightforward-with-explanation
# For every block of 2k characters starting with position i,
# we want to replace S[i:i+k] with it's reverse.
# In Python, slices are handled safely with respect to indices that are out of bounds.
