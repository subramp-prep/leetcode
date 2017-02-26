def reversePairs(self, nums):
  count = 0
  done = []
  for num in nums:
    count += len(done) - bisect.bisect(done, num * 2)
    bisect.insort(done, num)
  return count

# Only O(n^2), but has a decent chance to get accepted
# (just submitted five times, got 1919ms, TLE, TLE, TLE, 1969ms).
# https://discuss.leetcode.com/topic/79012
