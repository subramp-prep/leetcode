## 179. Largest Number (Medium)

### **链接**：
题目：https://leetcode.com/problems/largest-number  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个自然数数组，求这些数首尾相接可能组成的最大数。


### **分析**  
1. 自定义排序：时间复杂度O(nlogn)，空间复杂度O(1)或O(n)。
	- 将数视为字符串，并自定义排序，再首尾相连得到结果。
	- 排序方法：
		- 法1：依次比较各个位的数，若直到到达其中一个字符串尾端也比较不出值时：
			- 两字符串相等：结束比较；
			- 在一字符串长于另一个时：比较第一位和长字符串下一位的大小。
		- 法2：词典比较（lexicographic  comparation）s1+s2和s2+s1
	- 可以不创建字符串数组，仅在比较的时候转化为字符串，降低空间复杂度。