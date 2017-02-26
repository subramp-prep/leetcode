class Solution(object):

  def __init__(self):
    self.cnt = 0

  def reversePairs(self, nums):
    def msort(lst):          # h: beginning index of list
      # merge sort body
      L = len(lst)
      if L <= 1:                          # base case
        return lst
      else:                               # recursive case, pass the original index to merger
        return merger(msort(lst[:int(L / 2)]), msort(lst[int(L / 2):]))

    def merger(left, right):
      # merger
      new, l, r = [], 0, 0
      while l < len(left) and r < len(right):
        if left[l] <= 2 * right[r]:
          l += 1
        else:
          self.cnt += len(left) - l
          r += 1
      return sorted(left + right)

    msort(nums)
    return self.cnt

# Count "important reverse pairs" while doing mergesort:
# When we're doing mergesort, original index of elements in left part (smaller part), i, must less than those in right part, j.
# Simply compare nums[i] and 2*nums[j] and sum them up.

# https://discuss.leetcode.com/topic/78980
