class Solution(object):

    def maxSumSubmatrix(self, matrix, k):
        maxSum = -9999999
        horizontalSum = [[0 for j in xrange(0, len(matrix[0]) + 1)] for i in xrange(0, len(matrix))]
        for i in xrange(0, len(matrix)):
            for j in xrange(0, len(matrix[0])):
                horizontalSum[i][j] = horizontalSum[i][j - 1] + matrix[i][j]
        for cola in xrange(0, len(matrix[0])):
            for colb in xrange(cola, len(matrix[0])):
                bilist, vsum = [0], 0
                for i in xrange(0, len(matrix)):
                    vsumj = horizontalSum[i][colb] - horizontalSum[i][cola - 1]
                    vsum += vsumj
                    i = bisect.bisect_left(bilist, vsum - k)
                    if i < len(bilist):
                        maxSum = max(maxSum, vsum - bilist[i])
                    bisect.insort(bilist, vsum)
        return maxSum
