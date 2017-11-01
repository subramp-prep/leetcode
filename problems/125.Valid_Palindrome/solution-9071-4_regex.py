class Solution(object):

    def isPalindrome(self, s):
        s = re.sub(r"\W+", r"", s.lower())
        return s == s[::-1]
