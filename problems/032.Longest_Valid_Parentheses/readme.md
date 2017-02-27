## 032. Longest Valid Parentheses (Hard)

### **链接**：
题目：https://leetcode.com/problems/longest-valid-parentheses/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
问一个字符串里最长的合法括号串的长度。

### **分析**：

1. **(C++)**用栈来做，如果匹配就出栈，然后长度就是 `cur - stack_top_pos` 也就是 - 匹配的前一个位置。 O(n) time, O(n) space。
2. **(C++)**栈消耗空间太多了，其实可以维护 () 匹配的长度，不过可能出现 `()))` 和 `((()` 的情况，所以要前后各扫一遍。O(n) time, O(1) space。
3. 动态规划：
	假设dp[i+1]为开头到第i位字符之间最长括号的长度，那么分如下几种情况来讨论：
	a. 假如当前字符不为')'， 那么dp[i+1] = 0, 因为任何可用字符串都以')'结尾
	b. 假如当前字符为')', 还得分如下两种情况讨论
		i) 当前字符左边的字符为'(', 那么最大长度相当于扩大了2， 所以dp[i+1] = dp[i-1]+2
		ii) 当前字符左边的字符为')', 那么就相当于这样的例子： 
			()(()) 假设当前字符为最后一位，其左边的字符就是')'，那么我们先得找到i-1这个字符所代表的最大长度，所以就是i-1-dp[i], 
			然后发现这个位置如果是'('， 那么我们就把当前的最大长度扩增为i-1这个字符所代表的最大长度加上2， 
			计算完这一系列之后， 再加上之前已经存在过的最大长度dp[i-1-dp[i]], 在这个例子里面就相当于加上了开头的"()"长度。