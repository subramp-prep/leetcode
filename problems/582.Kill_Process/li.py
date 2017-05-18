# coding=utf-8
# Author: Jianghan LI
# Question: 582.Kill_Process
# Date: 2017-05-17 14:10 - 14:19
# Complexity: O(N)


class Solution(object):

    def killProcess(self, pid, ppid, kill):
        """
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        d = {}
        for c, p in zip(pid, ppid):
            if p not in d:
                d[p] = []
            d[p].append(c)
        bfs = [kill]
        for i in bfs:
            bfs.extend(d.get(i, []))
        return bfs

    def killProcess(self, pid, ppid, kill):
        d = collections.defaultdict(list)
        for c, p in zip(pid, ppid):
            d[p].append(c)
        bfs = [kill]
        for i in bfs:
            bfs.extend(d.get(i, []))
        return bfs
