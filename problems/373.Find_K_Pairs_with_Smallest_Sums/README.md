## 373. Find K Pairs with Smallest Sums (Medium)

### **链接**：
题目：https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给出两个从小到大排序的数组，要求给出两数组排列组合的整数对中，前k个和最小的。

### **分析**：
1. 暴力搜索（Brute Force）：时间复杂度O(k2)，空间复杂度O(k2)。  
最简单的思路，但是比较浪费：
	1. 创建所有可能对（每个数组取前k个即可）
	2. 按和的大小排序
	3. 输出前k个值

2. 优先队列（Priority Queue）：时间复杂度O(klogk)，空间复杂度O(k)。  
在暴力搜索的基础上优化了进行比较的数目，排序借助大小为k的优先队列来完成（按优先级插入一次复杂度是O(logk)），在需要提取的时候才插入新值。
	1. 建立pq储存数对的index，然后先放入nums1的所有index和nums2[0]的组合
	2. 然后建立一个while循环：
		* 取出pq顶部的index数对
		* 再插入一个可能次小的index数对，更新pq顶部值。
	* 过程图详见[leetcode解答](https://discuss.leetcode.com/topic/50885/simple-java-o-klogk-solution-with-explanation)