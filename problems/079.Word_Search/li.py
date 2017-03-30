# coding=utf-8
# Author: Jianghan LI
# Question: 079.Word_Search
# Date: 2017-03-24 01:16
# Complexity: O(N)


class Solution(object):

    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        m, n = len(board), len(board[0])

        def test(path, x, y):
            if 0 <= x < m and 0 <= y < n and (x, y) not in path and board[x][y] == word[len(path)]:
                if len(path) + 1 == len(word):
                    return True
                return any(test(path | set([(x, y)]), x + i, y + j) for i, j in ((1, 0), (-1, 0), (0, 1), (0, -1)))
            return False

        return any(test(set(), i, j) for i in range(m) for j in range(n))


############ test case ###########
s = Solution()
# print s.exist(["aa"], "a")
print s.exist(["CAA", "AAA", "BCD"], "AAB")  # True


############ comments ############
