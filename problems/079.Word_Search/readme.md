## 079. Word Search() (Medium)

### **链接**：

题目：https://leetcode.com/problems/word-search/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

在字符矩阵中中确认一个单词是否存在。相邻格子相连组成单词即可。

### **分析**：
 
1. 深度优先+回溯：时间复杂度O(m*n*4^k)，空间复杂度O(mn)。
	- 遍历矩阵，每个格子都深度优先搜索：
		1. 若当前格子数值不同，返回false。
		2. 向上下左右继续遍历。
	- 注意：已经核对的格子要标记，以免重复核对。