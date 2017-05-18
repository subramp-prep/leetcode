class Solution(object):

    def findSubsequences(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = set()
        for i in nums:
            for l in list(ret):
                if i >= l[-1]:
                    ret.add(l + (i,))
            ret.add((i,))
        return [l for l in ret if len(l) > 1]

############### test cases ###################
s = Solution()
print s.findSubsequences([1, 2, 3, 4])
