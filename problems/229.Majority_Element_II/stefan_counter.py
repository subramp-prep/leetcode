import collections


class Solution(object):

  def majorityElement(self, nums):
    ctr = collections.Counter()
    for n in nums:
      ctr[n] += 1
      if len(ctr) == 3:
        ctr -= collections.Counter(set(ctr))
    return [n for n in ctr if nums.count(n) > len(nums) / 3]

  def majorityElement2(self, nums, k):
    ctr = collections.Counter()
    for n in nums:
      ctr[n] += 1
      if len(ctr) == k:
        ctr -= collections.Counter(set(ctr))
    ctr = collections.Counter(n for n in nums if n in ctr)
    return [n for n in ctr if ctr[n] > len(nums) / k]

s = Solution()
print s.majorityElement([])
print s.majorityElement([3, 2, 3])
print s.majorityElement([1, 2, 1, 2, 5])


# majorityElement2:
# Generalization to ⌊N / k⌋, still O(N) time but O(k) space

# For the general problem, looking for elements appearing more than ⌊N /
# k⌋ times for some positive integer k, I just have to change my 3 to k.
# Then it already works and takes takes O(k) space and O(kN) time.

# The O(kN) time does not come from the main loop, though. Yes, each ctr
# -= ... does cost k, but I only have to do it at most N / k times. To put
# it in terms of the above explanation, I can't hide a vote more than
# once.


# No, the culprit is my last line, counting each remaining candidate
# separately. If I count them at the same time, I get O(N) again. Here's
# the full generalized code:

# https://discuss.leetcode.com/topic/17409
