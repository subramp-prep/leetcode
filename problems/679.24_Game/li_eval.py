import itertools

class Solution(object):

    def judgePoint24(self, nums):
        def f(s1, s2):
            res = []
            for a in s1:
                for b in s2:
                    res.append('(' + a + '+' + b + ')')
                    res.append('(' + a + '-' + b + ')')
                    res.append('(' + b + '-' + a + ')')
                    res.append(a + '*' + b)
                    res.append(a + '/' + b)
                    res.append(b + '/' + a)
            return res

        nums = [str(float(i)) for i in nums]
        for c in itertools.permutations(nums):
            eq1 = f(f(f([c[0]], [c[1]]), [c[2]]), [c[3]])
            eq2 = f(f([c[0]], [c[1]]), f([c[2]], [c[3]]))
            for eq in eq1 + eq2:
                try:
                    if 23.9 <= eval(eq) <= 24.1:
                        print eq.replace(".0", "")
                        return True
                except:
                    pass
        return False

############ test case ###########
s = Solution()
print s.judgePoint24([1, 8, 12, 12])
print s.judgePoint24([1, 2, 1, 2])
print s.judgePoint24([1, 9, 1, 2])
print s.judgePoint24([8, 1, 6, 6])


############ comments ############
# https://discuss.leetcode.com/topic/104030/python-useful-solution

# This is not a very efficace solution. Because it use evalfunction.
# In fact I wrote a function to help me find all solutions for 24 game.
# Efficacy was not that important. Then I met this problem I just modified
# my original solution to return just True or False
