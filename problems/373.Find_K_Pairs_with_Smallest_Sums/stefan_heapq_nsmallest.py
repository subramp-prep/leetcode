# coding=utf-8
# Author: Jianghan LI
# Question: /Users/mac/Work/LeetCode/problems/373.Find_K_Pairs_with_Smallest_Sums/li.py
# Date: 03/03/2017 00:47
# Complexity: O(N) O(N)

import itertools
import heapq


class Solution(object):

    def kSmallestPairs(self, nums1, nums2, k):
        streams = map(lambda u: ([u + v, u, v] for v in nums2), nums1)
        stream = heapq.merge(*streams)
        return [suv[1:] for suv in itertools.islice(stream, k)]

    def kSmallestPairs(self, nums1, nums2, k):
        queue = []

        def push(i, j):
            if i < len(nums1) and j < len(nums2):
                heapq.heappush(queue, [nums1[i] + nums2[j], i, j])
        push(0, 0)
        pairs = []
        while queue and len(pairs) < k:
            _, i, j = heapq.heappop(queue)
            pairs.append([nums1[i], nums2[j]])
            push(i, j + 1)
            if j == 0:
                push(i + 1, 0)
        return pairs


############ test case ###########
s = Solution()
print s.kSmallestPairs([1, 7, 11], [2, 4, 6], 3)
print s.kSmallestPairs([1, 1, 2], [1, 2, 3], 2)

############ comments ############
# Solution 4: Efficient(accepted in 112 ms)

# The brute force solutions computed the whole matrix(see visualization above).
# This solution doesn't. It turns each row into a generator of triples[u + v, u, v],
# only computing the next when asked for one.
# And then merges these generators with a heap.
# Takes O(m + k * log(m)) time and O(m) extra space.


# Solution 5: More efficient (accepted in 104 ms)

# The previous solution right away considered (the first pair of)
# all matrix rows (see visualization above). This one doesn't.
# It starts off only with the very first pair at the top-left corner of the matrix,
# and expands from there as needed.
# Whenever a pair is chosen into the output result,
# the next pair in the row gets added to the priority queue of current options.
# Also, if the chosen pair is the first one in its row,
# then the first pair in the next row is added to the queue.

# https://discuss.leetcode.com/topic/50450/slow-1-liner-to-fast-solutions
