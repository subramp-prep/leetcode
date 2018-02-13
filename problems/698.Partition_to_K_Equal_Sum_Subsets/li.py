class Solution(object):

    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        def dfs(nums, pos, target):
            if pos == len(nums):
                return True
            for i in range(k):
                if target[i] >= nums[pos]:
                    target[i] -= nums[pos]
                    if dfs(nums, pos + 1, target):
                        return True
                    target[i] += nums[pos]
            return False
        if len(nums) < k:
            return False
        numSum = sum(nums)
        nums.sort(reverse=True)
        if numSum % k != 0:
            return False
        target = [numSum / k] * k
        return dfs(nums, 0, target)

# 1800+ms, TLE sometimes
# just for k is small
