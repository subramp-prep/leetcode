# coding=utf-8
# Author: Jianghan LI
# Question: 514.Freedom_Trail
# Date: 09/03/2017


class Solution(object):

    def findRotateSteps(self, ring, key):
        # the distance between two points (i, j) on the ring
        def dist(i, j):
            return min(abs(i - j), len(ring) - abs(i - j))
        # build the position list for each character in ring
        pos = {}
        for i, c in enumerate(ring):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]
        # the current possible state: {position of the ring: the cost}
        state = {0: 0}
        for c in key:
            next_state = {}
            for j in pos[c]:  # every possible target position
                next_state[j] = float('inf')
                for i in state:  # every possible start position
                    next_state[j] = min(next_state[j], dist(i, j) + state[i])
            state = next_state
        return min(state.values()) + len(key)


s = Solution()
print s.findRotateSteps("abcde", "ade")  # 6
print s.findRotateSteps("godding", "godding")  # 13
print s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")  # 137
