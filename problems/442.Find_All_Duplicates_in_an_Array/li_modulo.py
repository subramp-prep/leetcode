class Solution(object):

  def findDuplicates2(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    n = len(nums)
    for x in nums:
      nums[x % n] += n
    return filter(lambda x: (nums[x % n] - 1) / n == 2, range(1, n + 1))
s = Solution()
print s.findDuplicates([4, 3, 2, 7, 8, 2, 3, 1])
print s.findDuplicates([2, 2])

# nums[i] = n * (i‘s occurence) ＋ nums[i]
# 正负号只能记录两个状态，同余可以记录多个。
# 但是，会有int超范围的问题，尽管test case没有出现。
