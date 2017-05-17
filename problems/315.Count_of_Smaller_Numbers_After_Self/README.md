## 315. Count of Smaller Numbers After Self (Hard)

### **链接**：
题目：https://leetcode.com/problems/count-of-smaller-numbers-after-self  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个数组，对每个值求此数后面小于它的数的个数，并输出数组。


### **分析**  
题目类别(Tags)：Divide and Conquer, Binary Indexed Tree, Segment Tree, Binary Search Tree  
最优复杂度(Complexity)：时间复杂度O(n)，空间复杂度O(n)。  


1. 暴力搜索（Brute Force）：时间复杂度O(n^2)，空间复杂度O(n)
	- 最简单的思路，但是会超时

2. 分治法（Divide&Conquer）+ 归并排序（Merge Sort）：时间复杂度O(nlogn)，空间复杂度O(n)
	- 分治思路：
		- Divide：从中间分割为数组，分为左表和右表
		- Conquer：归并过程中实现结果的储存：
			- 正在归并的左表的数的对应结果 += 右表已归并的数的个数
	- 需要数组来记录index的变化
	
3. 分治法（Divide&Conquer）+ 位操作：时间复杂度O(n)，空间复杂度O(n)
	- 分治思路：
		- Divide：利用位操作来比较数整数大小，二进制位从高到底，根据此位是0或1将数组分为高表和低表
		- Conquer：分割过程中实现结果的储存：
			- 区分出高表数时，此数对应结果 += 低表中的数数目
	- 注意对负数的位操作的处理
	- 时间复杂度和空间复杂度都是O(n),因为迭代深度是常数（整数的位数32）
	
4. 二叉搜索树（BST）：时间复杂度O(n^2)，θ(nlogn)，空间复杂度O(n)
	- 建立一个二叉搜索树，在插入每个节点时：
		- 左节点/值相等：++左侧节点的数目/++自身值出现次数
		- 右节点：递归来得得到多少在其左边的值
	- 数组从后向前遍历插入节点，并返回当前数对应值。
	- 复杂度：此算法有平均复杂度θ(nlogn)，而最坏情况时间复杂度为O(n^2)，一个从大到小排好序的的数组，如[100, 99, 98, ...., 3, 2, 1]，此时树高仍为n，并非nlogn
 
5. 平衡树（[Self-balancing BST](https://en.wikipedia.org/wiki/Self-balancing_binary_search_tree)）：时间复杂度O(nlogn)，空间复杂度O(n)
	- 在思路3的基础上，使用平衡树代替二叉搜索树，保证树高为logn，来保证O(nlogn)的复杂度。
	- 其它算法不变，只改变树的插入算法即可
	- 可选择的平衡树：
		1. [AVL树](https://en.wikipedia.org/wiki/AVL_tree)
		2. [红黑树](https://en.wikipedia.org/wiki/Red%E2%80%93black_tree)
	- 虽然最差时间复杂度更低，但是会TLE，因为在数随机排列的数组的test case中，由于多了平衡树高的步骤，所以并不占优势。

### **相关链接**
- Solutions for Count inversions in an array  :
	- [Merge Sort](http://www.geeksforgeeks.org/counting-inversions/)
	- [Self balancing BST](http://www.geeksforgeeks.org/count-inversions-in-an-array-set-2-using-self-balancing-bst/)
	- [Bits](http://www.geeksforgeeks.org/count-inversions-array-set-3-using-bit/) 