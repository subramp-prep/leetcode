# coding=utf-8
# Author: Jianghan LI
# Question: 689.Maximum_Sum_of_3_Non-Overlapping_Subarrays/li.py
# Complexity: O(N)
# Date: 2017-10-02


class Solution(object):

    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        maxsum = 0
        sum = [0]
        posLeft = [0] * n
        posRight = [n - k] * n
        ans = [0, 0, 0]
        for i in nums:
            sum.append(sum[-1] + i)
        # DP for starting index of the left max sum interval
        tot = sum[k] - sum[0]
        for i in range(k, n):
            if sum[i + 1] - sum[i + 1 - k] > tot:
                posLeft[i] = i + 1 - k
                tot = sum[i + 1] - sum[i + 1 - k]
            else:
                posLeft[i] = posLeft[i - 1]
        # DP for starting index of the right max sum interval
        tot = sum[n] - sum[n - k]
        for i in range(n - k - 1, -1, -1):
            if sum[i + k] - sum[i] > tot:
                posRight[i] = i
                tot = sum[i + k] - sum[i]
            else:
                posRight[i] = posRight[i + 1]
        # test all possible middle interval
        for i in range(k, n - 2 * k + 1):
            l = posLeft[i - 1]
            r = posRight[i + k]
            tot = (sum[i + k] - sum[i]) + (sum[l + k] - sum[l]) + (sum[r + k] - sum[r])
            if tot > maxsum:
                maxsum = tot
                ans = [l, i, r]
        return ans


############ test case ###########
s = Solution()
# print s.maxSumOfThreeSubarrays([1, 2, 1, 2, 6, 7, 5, 1], 2)
# print s.maxSumOfThreeSubarrays([7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3)
print s.maxSumOfThreeSubarrays([5, 5, 3, 3], 1)


############ comments ############
