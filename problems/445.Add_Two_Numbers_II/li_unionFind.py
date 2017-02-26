class Solution(object):

  def longestConsecutive(self, nums):
    length = len(nums)
    father = [i for i in range(length)]
    size = [1 for i in range(length)]

    def find(i):
      f = father[i]
      while f != father[f]:
        father[f] = father[father[f]]
        f = father[f]
      return f

    def union(a, b):
      root1, root2 = find(a), find(b)
      if root1 == root2:
        return
      if size[root1] < size[root2]:
        father[root1] = root2
        size[root2] += size[root1]
      else:
        father[root2] = root1
        size[root1] += size[root2]
    unionMap = {nums[i]: i for i in range(length)}
    for i in nums:
      if i - 1 in unionMap:
        union(unionMap[i], unionMap[i - 1])
      if i + 1 in unionMap:
        union(unionMap[i], unionMap[i + 1])
    ans = 0
    for i in size:
      ans = max(ans, i)
    return ans

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2])
