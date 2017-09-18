def hammingWeight(self, n, count=0):
    return self.hammingWeight(n & n-1, count+1) if n!=0 else count

def hammingWeight(self, n):
    return len([i for i in range(32) if (1<<i)&n])