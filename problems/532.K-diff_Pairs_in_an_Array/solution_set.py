def findPairs(self, nums, k):
    return len(set(nums) & {n + k for n in nums}) if k > 0 else sum(v > 1 for v in collections.Counter(nums).values()) if k == 0 else 0


def findPairs(self, nums, k):
    if k > 0:
        return len(set(nums) & set(n + k for n in nums))
    elif k == 0:
        sum(v > 1 for v in collections.Counter(nums).values())
    else:
        return 0
