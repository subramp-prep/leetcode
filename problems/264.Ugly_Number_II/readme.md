## 264. Ugly Number II (Medium)

### **链接**：
题目：https://leetcode.com/problems/ugly-number-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

给出一个整数n，给出第n大的Ugly Number。Ugly Number 是因子中只包含 2, 3, 5 的数。

### **分析**：

此题用动态规划可做：时间复杂度O(n)，空间复杂度O(n)。
	* 初始条件：dp[0] = 1
	* 求dp[i]：
		* 在前0..i-1项中*2, *3, *5，找下一个更大的值 
		* 遍历一遍寻找是可行的方法，可以存3个递增的index来进行优化