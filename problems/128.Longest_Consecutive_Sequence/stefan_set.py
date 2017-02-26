class Solution:

  def longestConsecutive(self, nums):
    nums = set(nums)
    maxlen = 0
    while nums:
      first = last = nums.pop()
      while first - 1 in nums:
        first -= 1
        nums.remove(first)
      while last + 1 in nums:
        last += 1
        nums.remove(last)
      maxlen = max(maxlen, last - first + 1)
    return maxlen

  def longestConsecutive2(self, nums):
    nums = set(nums)
    best = 0
    for x in nums:
      if x - 1 not in nums:
        y = x + 1
        while y in nums:
          y += 1
        best = max(best, y - x)
    return best


# longestConsecutive: set + pop searched ＋ search both sides
# https://discuss.leetcode.com/topic/10678/python-o-n-solution-using-sets/2


# longestConsecutive2: set ＋ search right
# First turn the input into a set of numbers.
# That takes O(n) and then we can ask in O(1)
# whether we have a certain number.

# Then go through the numbers.
# If the number x is the start of a streak
# (i.e., x - 1 is not in the set),
# then test y = x + 1, x + 2, x + 3, ... and
# stop at the first number y not in the set.

# The length of the streak is then simply y - x and
# we update our global best with that.

# Since we check each streak only once,
# this is overall O(n).
# This ran in 44 ms on the OJ,
# one of the fastest Python submissions.

# https://discuss.leetcode.com/topic/15383
