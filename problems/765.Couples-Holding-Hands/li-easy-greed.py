# 2018-05-08 16:42 - 16:50
class Solution(object):

    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        # print row
        if not row:
            return 0
        if abs(row[0] - row[1]) == 1 and max(row[0], row[1]) % 2 == 1:
            return self.minSwapsCouples(row[2:])
        if row[0] % 2:
            i = row.index(row[0] - 1)
            row[i], row[1] = row[1], row[i]
            return self.minSwapsCouples(row[2:]) + 1
        else:
            i = row.index(row[0] + 1)
            row[i], row[1] = row[1], row[i]
            return self.minSwapsCouples(row[2:]) + 1

    def minSwapsCouples(self, row):
        if not row:
            return 0
        i = row.index(row[0] + [1, -1][row[0] % 2])
        row[i], row[1] = row[1], row[i]
        return self.minSwapsCouples(row[2:]) + [1, 0][i == 1]

############ test case ###########
s = Solution()
# print s.minSwapsCouples([0, 2, 1, 3])  # 1
# print s.minSwapsCouples([3, 2, 0, 1])  # 0
print s.minSwapsCouples([6, 2, 1, 7, 4, 5, 3, 8, 0, 9])  # 0


############ comments ############
# 1 wrong try
