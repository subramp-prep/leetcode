# coding=utf-8
# Author: Jianghan LI
# Question: 609.Find_Duplicate_File_in_System
# Date: 2017-06-06 17:35 - 17:48, 1 wrong try
# Complexity: O(N)

import collections


class Solution(object):

    def findDuplicate(self, paths):
        """
        :type paths: List[str]
        :rtype: List[List[str]]
        """
        d = collections.defaultdict(list)
        for s in paths:
            s = s.split()
            root = s[0]
            files = s[1:]
            for f in files:
                f = f.split('(')
                d[f[1][:-1]].append(root + '/' + f[0])
        return [d[content] for content in d if len(d[content]) >= 2]

############ comments ############
# 1 wrong try: return only duplicates, not all files
