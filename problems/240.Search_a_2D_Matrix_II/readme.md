
## 240. Search a 2D Matrix II (Medium)

### **链接**：

题目：https://leetcode.com/problems/search-a-2d-matrix-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode  

### **题意**：

给出每行已经排好序的矩阵，要求判断某数是否存在其中。

### **分析**：

1. 二叉搜索树：时间复杂度O(m+n)，空间复杂度O(1)
	* 可将矩阵视为一个二叉搜索树，向右增大，向上减小
	* 先取左下角或者右上角的数为初始节点，比target小就向右，比target大就向左

2. 逐行二分法：时间复杂度O(mlog(n))，空间复杂度O(1)
	* 逐行用二分法判断target是否在行中
		
3. 分治法：时间复杂度O(m+n)^0.5~O((m+n)^1.4)之间，空间复杂度O(1)  
复杂度的计算详见文章[Searching a Sorted Matrix Faster](http://twistedoakstudios.com/blog/Post5365_searching-a-sorted-matrix-faster)
	* 逐渐把搜索范围缩小到矩阵中的一个长方形大小，直到剩最后一个数。
	* 使用递归法：
		- 初始条件：初始长方形就是原矩阵。
		- 递归思路：比较target和长方形中心的值k
			1. k == target：返回true
			2. k < target：说明不在右下部分，对剩下三个部分递归
			3. k > target：说明不在左上部分，对剩下三个部分递归
		- 结束条件：四个点不再构成长方形

### **相关问题**：
[074.Search_a_2D_Matrix](../074.Search_a_2D_Matrix)