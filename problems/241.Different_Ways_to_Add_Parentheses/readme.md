## 241. Different Ways to Add Parentheses (Medium)

### **链接**：
题目：https://leetcode.com/problems/different-ways-to-add-parentheses/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个不带括号的算术表达式，在不同的位置添加括号，会有不同的结果，要求输出所有可能结果。

### **分析**：
1. 分治法 + 递归法：时间复杂度O(2^n)，空间复杂度O(n*2^n)。
	- 遍历字符串，遇到符号时，将字符串左右分别当作相同的问题处理，递归得到左右结果，
	- 可以用`unordered_map<string,vector<int>>`，以substring为键值的哈希表来记录已经计算过的值，来降低复杂度：
		- 时间复杂度O(Cat(n))，空间复杂度O(n*Cat(n))
	- 复杂度的计算：
		- 时间复杂度是卡塔兰数O(Cat(n))：Cat(n) = C(2n, n)/(n + 1)，因为可能组合数：a(n)=a(0)*a(n)+a(1)*a(n-1)+...+a(n)*a(0)  
		- 因此空间复杂度，是时间复杂度的基础上，每次递归复制参数再乘以n：O(n*Cat(n))
	
2. 动态规划（DP）：时间复杂度O(Cat(n))，空间复杂度O(n^2*Cat(n))。
	- 此题想要用DP来解，就最好不使用string来构建DP表，string之间的比较比较复杂
	- 将所有的数和操作符从string中取出，然后再建立dp[i][j]储存从第i个数到第j个数所有可能的结果：
		- 初始化：dp[i][i] = {nums[i]}
		- 更新dp，(j:0->n，i:j->0)：dp[i][j] = dp[i][k] *+- dp[k + 1][j] (i < k < j)
		- 返回：dp[0][n - 1]