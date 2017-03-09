# coding=utf-8
# Author: Jianghan LI
# Question: 514.Freedom_Trail
# Date: 08/03/2017

import heapq


class Solution(object):

    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        pos = {}
        for i, c in enumerate(ring):
            if c in pos:
                pos[c].append(i)
            else:
                pos[c] = [i]
        h = [(0, 0, 0)]  # steps, ring pos, next char pos
        best = [float("inf")] * len(key)
        while 1:
            cur = heapq.heappop(h)
            # print cur
            if cur[2] == len(key):
                print best
                return cur[0] + len(key)
            for i in pos[key[cur[2]]]:
                diff = abs(cur[1] - i)
                step = min(diff, len(ring) - diff)
                next_step = (cur[0] + step, i, cur[2] + 1)
                # print cur, next_step
                if best[cur[2]] + len(ring) / 2 < next_step[0]:
                    continue
                best[cur[2]] = min(best[cur[2]], cur[0] + step)
                heapq.heappush(h, next_step)


s = Solution()
print s.findRotateSteps("abcde", "ade")  # 6
print s.findRotateSteps("godding", "godding")  # 13
print s.findRotateSteps("caotmcaataijjxi", "oatjiioicitatajtijciocjcaaxaaatmctxamacaamjjx")  # 137
