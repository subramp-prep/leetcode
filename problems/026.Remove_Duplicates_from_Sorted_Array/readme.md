## 026. Remove Duplicates from Sorted Array (Easy)

### **链接**：
题目：https://leetcode.com/problems/remove-duplicates-from-sorted-array/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个有序数列，删重复的元素。

### **分析**：
如果可以开一个数组来存就非常容易。但是这题不让用多余的空间。  
此题的关键是充分利用数组已排序这个特点。
	- 有重复值 == 相邻两值相等
	- 改造数组：把不重复的值移到对的位置