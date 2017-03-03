## 215. Kth Largest Element in an Array (Medium)

### **链接**：
题目：https://leetcode.com/problems/Kth-Largest-Element-in-an-Array/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
求一个数组里的第 k 大。

### **分析**：
1. 排序：最简单的思路是先将数组排序，再输出第n-k项。时间复杂度O(nlogn)，空间复杂度O(1)。

2. 使用特殊的数据结构：本质上还是排序。  
时间复杂度O(nlogn)，空间复杂度O(n)。
	* 优先队列（[priority queue](https://en.wikipedia.org/wiki/Priority_queue)）
	* 多重集（[multiset](https://en.wikipedia.org/wiki/Multiset)）
	* 堆

3. 快速选择算法：想法来源于快排。
时间复杂度Ω(n), O(n2), θ(n)，空间复杂度O(n)  
与快排相较（Ω(n), O(n2), θ(nlogn)），由于这里分割后只继续处理其中一边，所以期望时间复杂度会略小  
	* 递归:
		1. 选pivot，把数组分为两部分，大于pivot的数放左边，小于的放右
		2. 比较pivot的index和k，再其中选一部分继续分割
	* 终止条件：pivot的index为k

4. BFPRT算法(线性查找算法)：这个算法是在快速选择算法的基础上，对pivot的选择进行了优化，保证最坏情况下也有O(n)的复杂度  
时间复杂度O(nlog5)~O(n)，空间复杂度O(n)  
此题是典型的BFPRT算法应用题。  
	* 递归：
		1. 将n个元素划分为[n/5]组，每组5个元素，且至多只有一组由剩下的n mod 5个元素组成
		2. 寻找这[n/5]组每一组的中位数：任意方法排序->中位数
		3. 对第2歩得出的[n/5]个中位数，递归的调用select找出其中位数x，（偶数个中位数的情况下约定为选取中间小的一个）
		4. 把x看作pivot来分割数组。
		5. 
		   * 若i == k，返回x。
		   * 若i < k，在小于x的元素中递归查找第i小的元素。
		   * 若i > k，在大于x的元素中递归查找第i - k小的元素。
	* 终止条件：
		* 分割之前，n == 1时，返回当前值
		- 分割结束，i == k时，返回第i值

P.S. 此题在算法导论第九章有详解和证明