# coding=utf-8
# Author: Jianghan LI
# Question: 811.Subdomain_Visit_Count
# Complexity: O(N)
# Date: 2018-03-31 0:00:00 - 0:09:36, 0 wrong try


import collections
import re


class Solution(object):

    def subdomainVisits(self, cpdomains):
        """
        :type cpdomains: List[str]
        :rtype: List[str]
        """
        c = collections.Counter()
        for cp in cpdomains:
            n, a = cp.split()
            n = int(n)
            a = a.split('.')
            for i in range(len(a)):
                c['.'.join(a[i:])] += n
            print c
        return ["%d %s" % (c[k], k) for k in c]

    def subdomainVisits(self, cpdomains):
        c = collections.Counter()
        for cp in cpdomains:
            cd = re.split("[ .]", cp)
            for i in range(1, len(cd)):
                c['.'.join(cd[i:])] += int(cd[0])
        return ["%d %s" % (c[k], k) for k in c]

    def subdomainVisits(self, cpdomains):
        c = collections.Counter()
        for cd in cpdomains:
            n, s = cd.split()
            c[s] += int(n)
            for i in range(len(s)):
                if s[i] == '.':
                    c[s[i + 1:]] += int(n)
        return ["%d %s" % (c[k], k) for k in c]


############ test case ###########
s = Solution()
print s.subdomainVisits(["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"])


############ comments ############
# https://leetcode.com/problems/subdomain-visit-count/discuss/121738/C++JavaPython-Easy-Understand-Solution
