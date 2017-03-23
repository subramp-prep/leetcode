# coding=utf-8
# Author: Jianghan LI
# Question: 089.Gray_Code
# Date: 23/03/2017
# Complexity: O(1)


class Solution(object):

    def grayCode(self, n):
        class Gray(list):

            def __len__(self):
                return 2 ** n

            def __getitem__(self, i):
                return i ^ (i >> 1)
        return Gray()
