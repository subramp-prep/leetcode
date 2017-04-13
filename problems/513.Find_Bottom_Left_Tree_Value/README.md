## 513. Find Bottom Left Tree Value (Medium)

### **链接**：
题目：https://leetcode.com/problems/find-bottom-left-tree-value  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个二叉树，要求给出最下层的最左值。


### **分析**  
1. 广度优先搜索（BFS）+队列（Queue）：时间复杂度O(n)，空间复杂度O(n)。
	- 广度优先是最直观的思路。挨层遍历节点，将每层第一个值存入，直到最后一层。

2. 深度优先搜索（DFS）+堆（Stack）：时间复杂度O(n)，空间复杂度O(n)。
	- 深度优先搜索则需要一个全局变量，记录结果当前值是第几层的最左节点。
	- 在第一次遇到更下层的节点时，更新结果。
	- 因为堆是先进后出，所以先推右值，再推左值。

### **备注**
原题叫做 513.Find Left Most Element，
现在改为题意更明确的 513. Find Bottom Left Tree Value
