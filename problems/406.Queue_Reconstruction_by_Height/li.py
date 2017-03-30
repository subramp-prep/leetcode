# coding=utf-8
# Author: Jianghan LI
# Question: 406.Queue_Reconstruction_by_Height
# Date: 2017-03-30 11:41 - 12:00
# Complexity: O(N)


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        res = [(float('inf'), 0)]
        for p in sorted(people, key=lambda p: (p[1], p[0])):
            higher = 0
            for i in range(len(res)):
                higher += res[i][0] >= p[0]
                if higher > p[1]:
                    res.insert(i, p)
                    break
        return res[:-1]

    def reconstructQueue2(self, people):
        res = []
        for p in sorted(people, key=lambda p: (-p[0], p[1])):
            res.insert(p[1], p)
        return res

############ test case ###########
s = Solution()
print s.reconstructQueue([[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]])
# Output:[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
print s.reconstructQueue([[6, 0], [5, 0], [4, 0], [3, 2], [2, 2], [1, 4]])
# Output:[[4,0],[5,0],[2,2],[3,2],[1,4],[6,0]]


############ comments ############
