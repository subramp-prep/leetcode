import random
import numpy as np
# 1     Sample
# 5     len 5
# 10    len 10
# 20    len 100
# 10    len 1000
# 5     len 10000
# 1     len 1000 G = linked list
# 1     len 1000 G = [0]
f = open('1035.txt', 'w')
def pprint(A):
    #print (str(A).replace(' ',''))
    f.write(str(A).replace(' ', '').replace('\'', '\"') + "\n")

configs = [[5, 5], [10, 20], [20, 100], [10, 1000], [5, 10000]]
np.random.seed(None)
def Generate_TestCase(Size):
    A = np.random.permutation(Size).tolist()
    len_G = np.random.randint(Size) + 1
    G = np.random.choice(A, size=len_G, replace=False).tolist()
    pprint(A)
    pprint(G)
def Generate_ExtremeTestCase():
    A = np.random.permutation(1000).tolist()

    pprint(A)
    pprint(A)

    pprint(A)
    pprint("[0]")

for config in configs:
    [Cnt, Size] = config
    for i in range(Cnt):
        Generate_TestCase(Size)

Generate_ExtremeTestCase()
