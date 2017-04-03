class Solution(object):

    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        seen = set([])
        res = 0
        for i in range(len(M)):
            if i not in seen:
                toSee = [i]
                while len(toSee):
                    cur = toSee.pop()
                    if cur not in seen:
                        seen.add(cur)
                        toSee = [j for j, v in enumerate(M[cur]) if v and j not in seen] + toSee
                res += 1
        return res

# toSee = [j for j, v in enumerate(M[cur]) if v] + toSee
# 改成了 if v and j not in seen
# 提高了性能
