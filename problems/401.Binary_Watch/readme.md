## 401. Binary Watch (Easy)

### **链接**：
题目：https://leetcode.com/problems/binary-watch/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

给Binary Watch上亮灯的数目，要求给出所有可能表示的时间。

### **分析**：

1. 回溯+深度优先：时间复杂度O(n*2^n)
	- 用回溯来生成亮灯数目固定，所有可能值集合


2. 二进制法：时间复杂度O(1)，空间复杂度O(1)