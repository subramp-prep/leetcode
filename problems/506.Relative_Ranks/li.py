class Solution(object):

    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        def rank_name(i):
            if i == 0:
                return "Gold Medal"
            if i == 1:
                return "Silver Medal"
            if i == 2:
                return "Bronze Medal"
            return str(i + 1)
        pos = sorted(range(len(nums)), key=lambda i: -nums[i])
        rank = sorted(range(len(nums)), key=lambda i: pos[i])
        return map(rank_name, rank)

############ test case ###########
s = Solution()
print s.findRelativeRanks([5, 4, 3, 2, 1])
print s.findRelativeRanks([10, 3, 8, 9, 4])


############ comments ############
