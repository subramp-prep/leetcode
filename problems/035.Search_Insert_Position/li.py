# coding=utf-8
# Author: Jianghan LI
# Question: 035.Search_Insert_Position
# Date: 2017-05-06 10:45 - 10:45
# Complexity: O(logN)


class Solution(object):
    searchInsert = bisect.bisect_left
