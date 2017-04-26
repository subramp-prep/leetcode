# coding=utf-8
# Author: Jianghan LI
# Question: 338.Counting_Bits
# Date: 2017-04-26


class Solution(object):

    def countBits(self, num):
        class CountBits(list):

            def __getitem__(self, i): return bin(i).count('1')

            def __len__(self): return num + 1
        return CountBits()


# Class 里面要写list
