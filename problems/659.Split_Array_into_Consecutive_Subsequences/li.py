# coding=utf-8
# Author: Jianghan LI
# Question: 659.Split_Array_into_Consecutive_Subsequences
# Complexity: O(N)
# Date: 2017-08-13
# Contest 45, 0:34:22 - 1:04:47, 3 wrong try


class Solution(object):

    def isPossible(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        cur = [nums[0]]
        cur2 = []
        for a, b in zip(nums, nums[1:]):
            # print cur2, cur, a, b
            if b - a > 1:
                last = a
                if cur:
                    if not last + 1 - cur[-1] >= 3:
                        return False
                if cur2:
                    if not last - cur2[-1] >= 3:
                        return False
                cur = [b]
                cur2 = []

            if b - a == 1:
                if cur2:
                    if a - cur2[-1] >= 3:
                        cur2 = []
                    else:
                        return False
                if cur:
                    x = cur.pop()
                    cur2 = cur
                    cur = [x]
                else:
                    cur = [b]
            if b - a == 0:
                if cur2:
                    x = cur2.pop()
                    cur.append(x)
                    cur.sort()
                else:
                    cur.append(b)
        last = nums[-1]
        if cur:
            if not last + 1 - cur[-1] >= 3:
                return False
        if cur2:
            if not last - cur2[-1] >= 3:
                return False
        return True

    def isPossible(self, nums):
        nums = [-float('inf')] + nums + [float('inf')]
        cur, cur2 = [nums[0]],[]
        for a, b in zip(nums, nums[1:]):
            if b - a > 1:
                if cur and a + 1 - cur[-1] < 3: return False
                if cur2 and a - cur2[-1] < 3: return False
                cur, cur2 = [b], []
            if b - a == 1:
                if cur2 and a - cur2[-1] < 3: return False
                cur2 = cur
                cur = [cur2 and cur2.pop() or b]
            if b - a == 0:
                cur.append(cur2 and cur2.pop() or b)
                cur.sort()
        return True


############ test case ###########
s = Solution()
# print s.isPossible([1, 2, 3, 3, 4, 5])  # T
# print s.isPossible([1, 2, 3, 3, 4, 4, 5, 5])  # T
print s.isPossible([1, 2, 3, 4, 4, 5])  # F
# print s.isPossible([1, 2, 3, 4, 6, 7, 8, 9, 10, 11])  # F
# print s.isPossible([4, 5, 6, 7, 7, 8, 8, 9, 10, 11])  # T
# print s.isPossible()
# print s.isPossible()
# print s.isPossible()
# print s.isPossible()

############ comments ############
