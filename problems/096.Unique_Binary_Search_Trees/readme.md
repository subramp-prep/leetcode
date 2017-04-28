## 095. Unique Binary Search Trees II (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/unique-binary-search-trees-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode  
  
### **题意**：  
求拥有{1, 2, ..., n}这些节点的所有可能的二叉搜索树（BST)的个数。  
  
### **分析**：  
1. 深度优先搜索（DFS）+ 递归：时间复杂度O(2^n)，空间复杂度O(2^n)
	- 递归思路：
		- 结束条件：n==0或n==1，返回1
		- 递归：依次取1到i为根节点，递归求左树（i-1个节点）可能个数*递归求右树（n-i个节点）可能个数，再求和
	- 复杂度过高，会导致TLE。记忆已经计算过的数，时间复杂度可降至O(n^2)，空间复杂度O(n^2)

2. 动态规划(DP)：时间复杂度(n^2)，空间复杂度O(n)
	- 和思路1很相似
	- dp[i]储存，i个节点的BST个数：
		- 初始化：dp[0] = dp[1] = 1
		- 更新dp[i]：依次取1到i为根节点，左树（i-1个节点）可能个数*右树（n-i个节点）可能个数，再求和
		- 返回dp[n]

3. 卡塔兰数（[Catalan number](https://en.wikipedia.org/wiki/Catalan_number)）：时间复杂度O(n)，空间复杂度O(1)
	- 此题在[卡塔兰数的适用范围](http://www-math.mit.edu/~rstan/ec/catalan.pdf)之内，可直接用公式计算：Cat(n) = C(2n, n)/(n + 1)