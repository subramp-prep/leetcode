## 264. Ugly Number II (Medium)

### **链接**：
题目：https://leetcode.com/problems/ugly-number-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

给出一个整数n，给出第n大的Ugly Number。Ugly Number 是因子中只包含 2, 3, 5 的数。

### **分析**：

1. 暴力搜索：时间复杂度O(2^n*logn)，空间复杂度O(1)。时间复杂度非常高，会超时。
2. 用动态规划：时间复杂度O(n)，空间复杂度O(n)。
	* 初始条件：dp[0] = 1
	* 求dp[i]：
		* 在前0..i-1项中*2, *3, *5，找下一个更大的值 
		* 遍历一遍寻找是可行的方法，可以存3个递增的index来进行优化

3. 最小堆：时间复杂度O(nlogn)，空间复杂度O(1)。
	* 每次取堆中最小值，然后乘2, 3, 5，判断是否重复，再推入堆中,
		
### **相关问题**：
[263 Ugly Number](../263.Ugly_Number)  
[313 Super Ugly Number](../313.Super_Ugly_Number)