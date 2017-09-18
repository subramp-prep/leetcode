class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if t < 0: return False
        n = len(nums)
        d = {}
        w = t + 1
        for i in xrange(n):
            m = nums[i] / w
            if m in d:
                return True
            if m - 1 in d and abs(nums[i] - d[m - 1]) < w:
                return True
            if m + 1 in d and abs(nums[i] - d[m + 1]) < w:
                return True
            d[m] = nums[i]
            if i >= k: del d[nums[i - k] / w]
        return False


############ test case ###########
s=Solution()
print s.containsNearbyAlmostDuplicate([4,7,15],2,10)

############ comments ############
O(n) time O(n) space
The idea is like the bucket sort algorithm.
Suppose we have consecutive buckets covering the range of nums with each bucket a width of (t+1).
If there are two item with difference <= t, one of the two will happen:
(1) the two in the same bucket
(2) the two in neighbor buckets
