## 148.Sort List (Medium)

### **链接**：
题目：https://leetcode.com/problems/sort-list/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把一个链表升序排列。要求时间复杂度O(nlogn)，空间复杂度O(1)。

### **分析**：
链表的排序和数组的排序并在算法上无很大的差别，能用于数组的算法也同样可用于链表排序。
但两者在时间和空间的复杂度上有差别。维基百科中有一个表格总结。https://zh.wikipedia.org/wiki/%E6%8E%92%E5%BA%8F%E7%AE%97%E6%B3%95

1. 并归排序：有稳定的时间复杂度O(nlogn), 空间复杂度为O(1) （数组并归排序的空间复杂度为O(n)）
	- 一个小难点是如何得到链表的中点，这里可以设置一个步长为2的指针作为参照
2. 快速排序：时间复杂度O(n2), Ω(n), θ(nlogn)，并不稳定有超时的危险，间复杂度为O(1)
	- partition时，数组算法中有好几种确定pivot的方法，但由于链表的单向性，只有一种可行