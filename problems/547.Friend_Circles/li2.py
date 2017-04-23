# coding=utf-8
# Author: Jianghan LI
# Question: 547.Friend_Circles
# Date: 2017-04-20 09:12 - 0:21
# Complexity: O(N^2)


class Solution(object):

    def findCircleNum(self, M):
        seen = set()
        res = 0
        for i in range(len(M)):
            if i in seen:
                continue
            res += 1
            queue = [i]
            for j in queue:
                seen.add(j)
                for k, isfriends in enumerate(M[j]):
                    if isfriends and k not in seen:
                        queue.append(k)
        return res

    def findCircleNum2(self, M):
        seen = set()
        res = 0
        for i in range(len(M)):
            if i in seen:
                continue
            res += 1
            toSee = {i}
            while len(toSee):
                j = toSee.pop()
                seen.add(j)
                toSee.update(k for k, v in enumerate(M[j]) if v and k not in seen)
                if len(toSee) + len(seen) == len(M):
                    return res
        return res

    def findCircleNum3(self, M):
        seen = set()
        res = 0
        for i in range(len(M)):
            if i in seen:
                continue
            res += 1
            toSee = {i}
            while len(toSee):
                j = toSee.pop()
                seen.add(j)
                toSee.update(k for k, v in enumerate(M[j]) if v and k not in seen)
                if len(toSee) + len(seen) == len(M):
                    return res
        return res


############ test case ###########
s = Solution()
print s.findCircleNum2([[1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 1, 1, 1, 1, 1, 1]])
print s.findCircleNum2([[1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [1, 1, 1, 1, 1, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0, 0, 1]])
