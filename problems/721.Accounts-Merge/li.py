# coding=utf-8
# Author: Jianghan LI
# Question: 721.Accounts-Merge
# Complexity: O(N)
# Date: 2018-05 20:58 - 21:21, 0 wrong try

class Solution(object):

    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        parents = {}
        self.count = 0
        def add(x):
            if x not in parents:
                parents[x] = x
                self.count += 1
        def find(x):
            if x != parents[x]:
                parents[x] = find(parents[x])
            return parents[x]
        def union(x, y):
            x, y = find(x), find(y)
            if x != y:
                parents[x] = y
                self.count -= 1
                return True
            return False
        for account in accounts:
            name = account[0]
            emails = account[1:]
            add(name + ':' + emails[0])
            for e in emails[1:]:
                add(name + ':' + e)
                union(name + ':' + emails[0], name + ':' + e)
        res = {}
        for name_email in parents:
            name, email = name_email.split(':')
            root = find(name_email)
            if root not in res:
                res[root] = []
            res[root].append(email)
        return [[root.split(':')[0]] + sorted(res[root]) for root in res]


############ test case ###########
s = Solution()
print s.accountsMerge(accounts=[["John", "johnsmith@mail.com", "john00@mail.com"], ["John", "johnnybravo@mail.com"], ["John", "johnsmith@mail.com", "john_newyork@mail.com"], ["Mary", "mary@mail.com"]])
# [["John", 'john00@mail.com', 'john_newyork@mail.com', 'johnsmith@mail.com'],  ["John", "johnnybravo@mail.com"], ["Mary", "mary@mail.com"]]
