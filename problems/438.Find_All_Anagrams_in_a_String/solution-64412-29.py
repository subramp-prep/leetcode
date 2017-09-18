class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        res = []
        cnt = collections.Counter(p)
        cnt.subtract(s[:len(p) - 1])
        for i in range(len(p) - 1, len(s)):
            cnt.update({s[i]: -1})
            if not any(cnt.values()):
                res.append(i - len(p) + 1)
            cnt.update({s[i - len(p) + 1]: 1})
        return res