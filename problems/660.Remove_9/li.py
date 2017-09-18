# coding=utf-8
# Author: Jianghan LI
# Question: 660.Remove_9
# Complexity: O(N)
# Date: 2017-08-13
# Contest 45, 0:20:00 - 0:34:22, 1 wrong try


class Solution(object):

    def newInteger(self, n):
        """
        :type n: int
        :rtype: int
        """
        def decimalToAny(num, n):
            baseStr = {10: "a", 11: "b", 12: "c", 13: "d", 14: "e", 15: "f", 16: "g", 17: "h", 18: "i", 19: "j"}
            new_num_str = ""
            while num != 0:
                remainder = num % n
                if 20 > remainder > 9:
                    remainder_string = baseStr[remainder]
                elif remainder >= 20:
                    remainder_string = "(" + str(remainder) + ")"
                else:
                    remainder_string = str(remainder)
                new_num_str = remainder_string + new_num_str
                num = num / n
            return new_num_str
        return int(decimalToAny(n, 9))

############ test case ###########
s = Solution()
print s.newInteger(9)

############ comments ############
