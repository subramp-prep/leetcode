## 022.Generate Parentheses (Medium)

### **链接**：
题目：https://leetcode.com/problems/generate-parentheses/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出需要的括号对数，生成包含所有可能的成对的"("")"的字符串组

### **分析**：
1. 递归法：
	对产生string的过程进行递归，每个递归结束时向结果中加入此string。
	生成string的规则：每次递归添加"("或")"，并确保
		- 添加"("和")"各n个
		- 在添加")"之前已有对应的"("添加
2. 迭代法(DP)：
	建立一个大小为n的数组，一步一步储存括号对数为1..n的结果，第i步的可以在前1..i-1歩的基础上取得，原理大致如下 ：
	step_0 ""
	step_1, "(s0)"
	step_2, "(s0)s1" "(s1)s0"
	step_3, "(s0)s2" "(s1)s1" "(s2)s0"
	...

PS. 算法复杂度 == 结果中string个数：