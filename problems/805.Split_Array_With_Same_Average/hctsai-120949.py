class Solution(object):

    def _GenerateCombinationSum(self, A, sum_set):
        """Stores all the comibnation sum into sum_set.

        Args:
          A: the array to be calcualting the sum of all combinations
          sum_set: the set that stores all possible summation values

        Returns:
          True if there is some partial sum equals to zero. False, otherwise.
        """
        for u in A:
            new_sum_set = set()
            for v in sum_set:
                if u + v == 0:
                    return True
                new_sum_set.add(u + v)
            sum_set |= new_sum_set
        return False

    def splitArraySameAverage(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        # Shortcuts for corner cases
        if len(A) == 1:
            return False
        if len(A) == 2:
            return A[0] == A[1]

        A_sum = sum(A)
        A_len = len(A)

        # Normalize the array so we only deal with integer calculation
        normalized_A = [A_len * v - A_sum for v in A]

        mid_way_begin = (A_len) / 2

        left_sum = set([0])
        if self._GenerateCombinationSum(normalized_A[:mid_way_begin], left_sum):
            return True

        right_sum = set([0])
        if self._GenerateCombinationSum(normalized_A[mid_way_begin:-1], right_sum):
            return True

        for v in left_sum:
            if v == 0:
                continue
            if -v in right_sum:
                return True
        return False


# https://leetcode.com/problems/split-array-with-same-average/discuss/120949/Simple-python-code-with-explanation/119917?page=1


# Li's comments:
# I did the part of subtracting each element by the average. Keep it in integer instead of float is a good idea.
# The idea of to calculate left and right separately is really tricky and it works.
# Upvoted.
