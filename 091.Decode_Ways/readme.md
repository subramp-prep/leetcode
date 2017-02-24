## 091. Decode Ways (Medium)

### **链接**：
题目：https://leetcode.com/problems/decode-ways/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个数字字符串（包括0），将其看成英文字母的序号相连接，求其可能代表的字母序列的个数。
例如给"12", 结果为2："AB" (1 2) 和 "L" (12)。

### **分析**：
动态规划可做。
	- 初始条件：
		dp[0] = 1;
		dp[1] = 第一个字符代表数字不为0
	- 迭代：
		dp[i] = dp[i - 1] （若当前字符代表数字不为0）
		  + dp[i - 2] （若当前字符和前一个字符所代表数字 i.是两位数 ii. <= 26）
P.S.
- 可以优化空间为O(1)
- 同样的思路写出递归代码，不过复杂度高无法ac