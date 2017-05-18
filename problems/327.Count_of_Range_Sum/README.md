## 327. Count of Range Sum (Hard)

### **链接**：
题目：https://leetcode.com/problems/count-of-range-sum  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一数组和一数值范围（上下界值），求此数组在此范围的，子区间的数值和的个数。


### **分析**  
题目类别(Tags)：Divide and Conquer, Binary Search Tree  
最优复杂度(Complexity)：时间复杂度O(nlogn)，空间复杂度O(n)  

1. 暴力搜索：时间复杂度O(n^2)，空间复杂度O(1)
	- 最简单的思路，两个for循环即可
	
2. 分治法（Divide&Conquer）+归并排序（merge sort）：时间复杂度O(nlogn)，空间复杂度O(n)
	- 分治思路：
		- Divide：从中间分割为数组，分为左表和右表，分别排序
		- Conquer：归并过程中实现结果的储存，双指针的思路：
			- 此时左右表已经排序，子表的对应结果也已经返回，所以现在只需要求出横贯左右表的在[lower, upper]范围的sums[j]-sums[i]个数
			- i遍历左表，j遍历右表求出的右表sums[j]-sums[i]在[lower, upper]边界值[m, n] => n - m即是所求值

3. 二叉搜索树（BST）：时间复杂度O(n^2)，θ(nlogn)，空间复杂度O(n)
	- 基本思路：
		- 使用BST来储存sum[i]=nums[0]+..+nums[i]，子区间[i,j]的值的和就是sums[j]-sums[i]
		- 所以，在插入sums[j]时，先判断有多少sums[j]-sums[i]是属于[lower, upper]范围的，并返回此值
		- lower <= sums[j]-sums[i] <= upper 可转化为：
			- 在[sums[j] - upper, sums[j] - lower]范围的sum个数
			- 即index(sums[j]-lower) - index(sums[j]-upper)数目
			
4. 平衡树（Balanced Binary Tree）: 时间复杂度O(nlogn)，空间复杂度O(n)
	- 算法与BST基本相同，就是在插入节点时再加入树的平衡算法
	- 可选择的平衡树：红黑树，AVL树
	- 使用平衡树，可以保证树高为logn，所以最坏情况下复杂度也有O(nlogn)，但仍然会超时。


### **相关问题**  
[315.Count_of_Smaller_Numbers_After_Self](../315.Count_of_Smaller_Numbers_After_Self)