## 434. Number of Segments in a String (Easy)

### **链接**：
题目：https://leetcode.com/problems/number-of-segments-in-a-string
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个字符串，求其中被空格所分开的子字符串个数

### **分析**：
本题唯一要注意的是如何处理子字符串之间复数空格。
1. while和if，直接模拟
2. C++中可以用istringstream来处理空格。