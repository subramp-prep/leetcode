# coding=utf-8
# Author: Jianghan LI
# Question: 164.Maximum_Gap
# Date: 2017-04-09
# Complexity: O(N)


def maximumGap(self, num):
    if len(num) < 2 or min(num) == max(num):
        return 0
    a, b = min(num), max(num)
    size = (b - a) // (len(num) - 1) or 1
    bucket = [[None, None] for _ in range((b - a) // size + 1)]
    for n in num:
        b = bucket[(n - a) // size]
        b[0] = n if b[0] is None else min(b[0], n)
        b[1] = n if b[1] is None else max(b[1], n)
    bucket = [b for b in bucket if b[0] is not None]
    return max(bucket[i][0] - bucket[i - 1][1] for i in range(1, len(bucket)))

# 抽屉原理，分成至少N－1个抽屉，记录每个抽屉内的最大数和最小数。
# 抽屉内的gap肯定小于抽屉大小，而且肯定有空抽屉，所以不需要考虑抽屉内的gap
