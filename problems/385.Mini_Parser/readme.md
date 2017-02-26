## 385. Mini Parser

### **链接**：

题目：https://leetcode.com/problems/mini-parser/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
将形式为"[123,[456,[789]]]"的字符串，转换为NestedInteger（题目定义的数据结构）

### **分析**：
1. 迭代法：建立stack:
	- 遇到左括号时，存入一个NestedInteger()
	- 遇到数字时，转化为数字，赋值到顶端的NestedInteger
	- 遇到右括号时，取出顶端的NestedInteger，连到下层的NestedInteger上
	时间复杂度O(n), 空间复杂度O(n)
2. 递归法：
	- 结束条件：空字符串，数字字符串
	- 遇到数字：把数字部分作为input递归
	- 遇到左括号：把左括号到对应右括号部分作为input递归
	时间复杂度O(n), 空间复杂度O(1)