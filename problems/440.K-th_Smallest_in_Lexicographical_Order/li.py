class Solution(object):

    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        def steps(cur, n):
            count = 0
            left, right = cur, cur + 1
            while left <= n:
                count += min(n + 1, right) - left
                left, right = 10 * left, 10 * right
            return count

        def steps(cur, n):
            dif = 10 ** (len(str(n)) - len(str(cur)))
            return dif / 9 + min(max(n - cur * dif + 1, 0), dif)

        res = 1
        k -= 1
        while k > 0:
            count = steps(res, n)
            if k >= count:
                res += 1
                k -= count
            else:
                res *= 10
                k -= 1
        return res


############ test case ###########
s = Solution()

# print s.findKthNumber(2, 1) #1
# print s.findKthNumber(2, 2) #2
# print s.findKthNumber(12, 2)  # 10
# print s.findKthNumber(13, 2)  # 10
# print s.findKthNumber(100, 10)  # 10
print s.findKthNumber(4289384, 1922239)


############ comments ############
