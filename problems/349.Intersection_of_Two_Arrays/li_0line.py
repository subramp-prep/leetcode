# coding=utf-8
# Author: Jianghan LI
# Question: 349.Intersection_of_Two_Arrays
# Date: 2017-04-03
# Complexity: O(M+N)


class Solution(object):

    intersection = lambda *p: list(set(p[1]) & set(p[2]))
