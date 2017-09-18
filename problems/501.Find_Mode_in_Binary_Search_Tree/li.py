class Solution(object):
    def checkPossibility(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        index = -1
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                if index >= 0:
                    return False
                else:
                    index = i
        if i==0 or i==len(nums)-2: return True
        if nums[i-1]<=nums[i+1] or nums[i]<=nums[i+2]: return True
        return False


