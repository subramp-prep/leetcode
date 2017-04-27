## 338. Counting Bits (Medium)

### **链接**：
题目：https://leetcode.com/problems/counting-bits  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个非负整数n，求给出从0到此数，2进制中1的数目。要求时间复杂度O(n)，只允许进行0到n一次遍历。


### **分析**  
1. 暴力搜索（Brute Force）：时间复杂度O(n*sizeof(int))，空间复杂度O(n)
	- 若不要求遍历次数，则暴力搜索是很容易想到的思路
	
2. 动态规划（DP）：时间复杂度O(n)，空间复杂度O(n)
	- 一个整数n的2进制1个数可以从小于它的数得来，有几种思路：
		1. n>>1(n/2)的1的个数，再以n&1(n%2)判断最后一位bit是不是1
		2. 比n&(n-1)的1的个数多1