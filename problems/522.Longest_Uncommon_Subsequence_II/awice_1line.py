class Solution(object):

    def findLUSlength(self, A):
        return max([len(w1) for i, w1 in enumerate(A)
                    if all(not all(c in z2 for c in w1)
                           for j, z2 in enumerate(map(iter, A)) if i != j)]
                   or [-1])
