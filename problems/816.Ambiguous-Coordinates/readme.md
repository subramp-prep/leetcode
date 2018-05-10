816.Ambiguous_Coordinates
----------------------------------------------

###**Links**：
Problem: https://leetcode.com/problems/Ambiguous-Coordinates
Solution: https://github.com/JianghanLi/LeetCode/problems/816.Ambiguous_Coordinates
Discuss: https://leetcode.com/problems/ambiguous-coordinates/discuss/123851


###**Discuss**：
We can split S to two parts for two coordinates.
Then we use sub function ```f``` to find all possible strings for each coordinate.

**In sub functon f(S)**
if S == "": return []
if S == "0": return [S]
if S == "0XXX0": return []
if S == "0XXX": return ["0.XXX"]
if S == "XXX0": return [S]
return [S, "X.XXX", "XX.XX", "XXX.X"...]

Then we add the product of two lists to result.

**Time complexity**
O(N^3) with N <= 10


Provement:

- latex:
\begin{aligned}\sum_{k=1}^{n} (n-k+1)k = (n+1)\sum_{k=1}^{n}k-\sum_{k=1}^{n}k^2= (n+1)\left[ \frac{1}{2} n (n+1)\right]-\frac{1}{6}n (n+1) (2 n+1) = \frac{1}{6}n (n+1) (n+2).\end{aligned}

- s3 img:
![image](https://s3-lc-upload.s3.amazonaws.com/users/lee215/image_1523920967.png)