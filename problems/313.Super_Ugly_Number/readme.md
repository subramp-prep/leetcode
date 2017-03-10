## 264. 313. Super Ugly Number (Medium)

### **链接**：
题目：https://leetcode.com/problems/super-ugly-number/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

给出一个整数n，和一个质数数组，给出第n大的Super Ugly Number。Super Ugly Number 是因子中只包含数组中质数的数。

### **分析**：

1. 动态规划：时间复杂度O(nk)，空间复杂度O(n)。  动态规划的思路非常类似[Ugly Number II]((../264.Ugly_Number_II))
	* 创建与primes数组等长的prime index数组。
	* 初始条件：dp[0] = 1
	* 求dp[i]：
		* 遍历第一遍，找到最小ugly number。
		* 遍历第二遍，更新最小ugly number对应的prime index值。
		
		
2. 最小堆算法
		
### **相关问题**：

[263 Ugly Number](../263.Ugly_Number)  
[264 Ugly Number II](../264.Ugly_Number_II)