
## 221. Maximal Square (Medium)

### **链接**：
题目：https://leetcode.com/problems/maximal-square/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

求一个 01 矩阵中的最大正方形的面积。

### **分析**：

如果直接做是枚举正方形的起点，再枚举边长，复杂度是 O(n^4)，不可能过的。  
一看就知道是 DP。  

1. 开 3 个辅助数组，跟地图一样大小，一个记录从当前位置往上走有几个 1，一个记录往左走有几个，一个就是 DP 数据。先处理出前两个数组，然后 DP 式就是 `dp[i][j] = min(dp[i-1][j-1]+1, up[i][j], left[i][j])`，时间用了 O(n)。
2. 对 1 解法优化空间，只要开一维的数组就行了，用滚动数组进行降维。
3. 这题可以暴力搞的（我的基友搞过了），枚举长度，然后把不能构成正方形的点标为 0，这样之后就可以跳过了。
4. 看了 Discuss 后发现他们用的 DP 很神奇：`dp[i][j] = min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1 if (i,j) == 1`，其实不难想，因为那三个位置只要有一个值不够大就不能，那 dp[i][j] 也不可能变大的。
