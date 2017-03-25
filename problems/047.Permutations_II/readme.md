## 047. Permutations II (Medium)

### **链接**：
题目：https://leetcode.com/problems/permutations-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个有重复数的数组，要求给出所有数调换位置可能情况。

### **分析**：
此题与46题解法类似，关键在于如何处理重复数字

1. 深度优先搜索：时间复杂度O(n!)，空间复杂度O(n*n!)。
	- 思路：
		- permutate([1...n]) = [1]permutate([2...n]) + [2]permutate([1,3...n]) + ... + [k]permutate([1...k-1,k+1,...n]) + ...
		- 同时保证1...k中没有重复。
	- 步骤：
		- 递归起点：原数组，0为原集合遍历起点，输入迭代函数
		- 递归过程：
			- 从集合起点for循环，遍历输入的数组，若有重复跳过，否则交换集合起点和遍历到的数，输入迭代函数
		- 结束条件：集合起点到达集合尾端，放入输入的数组。
	- 注意：如何判断重复很关键，有两种方式，都会使空间复杂度升至O(n*n!)：
		1. 数组不再以reference的方式输入，而是复制输入。在返回时不再对数组还原，即swap之后不再swap back，比较nums[start]和nums[i]即是判断重复。
		2. 使用unordered_set来判断重复，并在返回时还原数组。时间复杂度同时会升至O(logn*n!)  
		可见第一种方法更好。
		
2. 迭代法-添加：时间复杂度O(n*n!)，空间复杂度O(n)。
	- 思路：遍历数组nums，当遍历到nums[i]时，结果中是nums[0]至nums[i-1]的全排列。
	- 步骤：
		0. 初始化，res中放入空集
		1. 第一个for循环：遍历nums，取nums[i]
		2. 第二个for循环：遍历res中存在的数组res[j]
		3. 第三个for循环：
			- 每个数组在位置k（0...res[j].size()）分别插入nums[i]，再放入res
			- 添加判断重复的条件：k > 0 && res[j][k-1] == nums[i]时，说明出现重复，跳过 => 只在k为0时插入一次即可
	
### **相关问题**：
[046.Permutations](../046.Permutations)