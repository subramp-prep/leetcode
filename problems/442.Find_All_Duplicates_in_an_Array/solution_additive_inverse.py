class Solution(object):

  def findDuplicates(self, nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    res = []
    for x in nums:
      if nums[abs(x) - 1] < 0:
        res.append(abs(x))
      else:
        nums[abs(x) - 1] *= -1
    return res

# when find a number i, flip the number at position i - 1 to negative.
# if the number at position i - 1 is already negative,
# i is the number that occurs twice.
