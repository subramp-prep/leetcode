class Solution(object):

  def twoSum(self, nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    if len(nums) <= 1:
      return False
    seen = {}
    for i in range(len(nums)):
      if nums[i] in seen:
        return [seen[nums[i]], i]
      else:
        seen[target - nums[i]] = i

  ############### test cases ###################
  # print twoSum(object, [2, 7, 11, 15], 9)
  print twoSum(object, [-1, -2, -3, -4, -5], -8)
  print twoSum(object, [3, 2, 4], 6)

  # Complexity: O(n)
  # Tag: Hash Table
