## 130. Surrounded Regions (Medium)

### **链接**：
题目：https://leetcode.com/problems/surrounded-regions/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个地图，把地图里被 X 包围的 O 块填充为 X。

### **分析**：
此题可以进行一个思路转换进行简化: 1. 除了没被包围的O就只剩被包围了的O。2. 没被包围的O都直接或通过O与边界上的O相连。  
这样就省去了很多的检查过程。

1. 深度优先搜索（DFS）：时间复杂度O(mn)，空间复杂度O(mn)
	- 从边界上遇到的O开始，调用DFS，将所有的相邻O都标记为不能被填充。
	- 遍历矩阵，把未标记的O变成'X'。
	- 注意：递归此题可能会导致runtime error，是递归导致的stack overflow。在dfs递归中，不再重复判断边界值可以避免。

2. 广度优先搜索（BFS）+队列（Queue）：时间复杂度O(mn)，空间复杂度O(mn)
	- 思路同上，使用队列转化为迭代法。