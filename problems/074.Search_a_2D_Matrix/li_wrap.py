import bisect


def searchMatrix(self, matrix, target):
    class Wrap:

        def __getitem__(self, i): return matrix[i / len(matrix[0])][i % len(matrix[0])]

        def __len__(self): return len(matrix[0]) * len(matrix)
    return any(matrix) and Wrap()[bisect.bisect(Wrap(), target) - 1] == target

s = Solution()
print s.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 50]], 3)
