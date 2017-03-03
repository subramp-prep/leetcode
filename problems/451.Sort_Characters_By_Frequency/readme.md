## 451. Sort Characters By Frequency (Medium)

### **链接**：
题目：https://leetcode.com/problems/sort-characters-by-frequency/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把字符串中的字母按出现频率排列。

### **分析**：
此题分为两个步骤：
	1. 记录字母出现频率
		- HashMap，Array等结构都可以
	2. 按频率排序，再输出
		- O(nlogn)排序：priority queue, heap, ...
		- 桶排序（[Bucket sort](https://en.wikipedia.org/wiki/Bucket_sort)）