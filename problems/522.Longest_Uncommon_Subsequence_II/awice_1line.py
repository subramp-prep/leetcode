class Solution(object):

    def findLUSlength(self, A):
        return max([len(w1) for i, w1 in enumerate(A)
                    if all(not all(c in z2 for c in w1)
                           for j, z2 in enumerate(map(iter, A)) if i != j)]
                   or [-1])

    # improved by Jianghan
    def findLUSlength(self, strs):
        return max([len(s1) for s1 in strs
                    if sum(all(c in it for c in s1) for it in map(iter, strs)) == 1]
                   or [-1])
