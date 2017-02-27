## 025. Reverse Nodes in k-Group (Hard)

### **链接**：
题目：https://leetcode.com/problems/reverse-nodes-in-k-group/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把一个链表每 k 个分为一组，每组内进行翻转。
只能用常数级的空间。

### **分析**：

这题比较考验链表的操作。
1. 递归法：先找到下一组的节点，把本组反转后再递归处理后面的节点。并非尾递归。
2. 迭代法：提前求出有几组k，再建立两个for循环。