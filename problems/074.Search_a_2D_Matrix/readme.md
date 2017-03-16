
## 074. Search a 2D Matrix (Easy)

### **链接**：
题目：https://leetcode.com/problems/search-a-2d-matrix/  
代码(github)：https://github.com/JianghanLi/LeetCode  

### **题意**：
给出已经排好序的矩阵，每行第一个大于上一行最后一个，要求判断某数是否存在其中。

### **分析**：
1. 扫描数组：时间复杂度O(m+n)，空间复杂度O(1)
	* 先判断在哪行，再判断是否存在于此行中
	* 左上，右上，左下，右下均可为起点

2. 二分法：时间复杂度O(log(m)+log(n))，空间复杂度O(1)
	* 先用二分法判断在哪行，再在此行中用二分法判断是否存在
	
3. 二分法 + 压缩数组：时间复杂度O(log(mn))，空间复杂度O(1)
	* 把整个矩阵当作一个一维数组，用二分法判断是否存在

P.S. 思路2和3，复杂度是等价的，O(log(m)+log(n) == O(log(mn))