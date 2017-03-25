def permuteUnique(self, nums):
    return [[n] + p for n in set(nums) for p in self.permuteUnique(nums[:nums.index(n)] + nums[nums.index(n) + 1:])] or [[]]


# https://discuss.leetcode.com/topic/38971/1-line-python-solution-set-list-slicing-beats-46-11
