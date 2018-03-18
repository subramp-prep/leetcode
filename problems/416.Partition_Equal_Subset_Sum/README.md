## 416. Partition Equal Subset Sum (Medium)

### **链接**：
题目：https://leetcode.com/problems/partition-equal-subset-sum  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个非空正数数组，求是否能分割成两个和相同的数组。


### **分析**  
1. 深度优先搜索（DFS）：时间复杂度O(2^n)，空间复杂度O(2^n)。
	- 递归思路：dfs看数组中各个值累加，看能不能够得到array总和的一半的值
		- 递归起点：target = sum / 2
		- 递归情况：
			- target为0，返回true
			- target为负，则当前值不符合要求，无需继续，返回false
			- target为正，target减去当前值，继续递归下一个值
	- 此题有几个降低复杂度的办法，可以通过test：
		1. 写成尾递归形式
		2. 提前将数组排序
		3. 设置全局变量通过记忆已算结果（和DP类似，不过会导致空间大幅度复杂度增加，运行一些简单的test会变慢，所以对于本题的test case，前两个优化已经足够）。
	
3. 动态规划（DP）：时间复杂度O(sum(nums)*n) < O(200*100*n)~O(1)，空间复杂度O(sum(nums)) < O(200*100)~O(1)。
	- dp[i] = {true, false}，记录一个target是否能是几个数之和：
		- 初始化：dp[0] = true
		- 更新：遍历数组，再从target到当前数更新：dp[i] = dp[i] || dp[i - n];
		- 返回：dp[sum(nums) / 2]。

4. 二进制数组（Bitset）：时间复杂度O(n)，空间复杂度O(const)~O(1)。
	- 思路和DP一样，用bitset代替DP中的bool值数组。