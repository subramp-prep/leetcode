## 61.Rotate List (Medium)

### **链接**：
题目：https://leetcode.com/problems/rotate-list/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出链表和整数k，要求把从右数k个数移到最前面

### **分析**：
因为k的值有可能大于链表长度，要求链表长度进行求余。
1. 连成环，找第l - k % l个节点
2. 用步长不同的双指针