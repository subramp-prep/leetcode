# coding=utf-8
# Author: Jianghan LI
# Question: 386.Lexicographical_Numbers
# Complexity: O(N)
# Date: 2017-08-22

class Solution(object):
    # Sort, Memory Limit Exceeded at n = 49999
    def lexicalOrder(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        return sorted(xrange(1,n+1),key=lambda x: str(x))

    #DFS，Time Limit Exceeded at n = 14959
    def lexicalOrder(self, n):
        def dfs(x, n, ret):
            if x > n: return
            ret.append(x)
            x *= 10
            for i in range(10):
                dfs(x+i, n, ret)
        ret = []
        for i in range(1,10):
            dfs(i, n, ret)
        return ret

    #根据discuss改变
    def lexicalOrder(self, n):
        ans = []
        x = 1
        for _ in range(n):
            ans.append(x)
            if x * 10 <= n:
                x *= 10
            else:
                while x % 10 == 9 or x == n: x /= 10
                x += 1
        return ans




############ test case ###########
s=Solution()
print s.lexicalOrder(13)

############ comments ############

