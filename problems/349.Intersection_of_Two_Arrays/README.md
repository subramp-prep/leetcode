## 349. Intersection of Two Arrays (Easy)

### **链接**：
题目：https://leetcode.com/problems/intersection-of-two-arrays  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
求两个数组交集

### **分析**  
1. 哈希表（HashTable）：时间复杂度O(n+m)，空间复杂度O(n)
	- 遍历数组，用HashTable(HashSet)记录。若再次出现则放入结果，并去掉此值避免重复。

2. 排序：时间复杂度O(n2)，空间复杂度O(1)
	- 先将两个数组排序，然后再比较。