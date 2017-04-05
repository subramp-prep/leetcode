## 056. Merge Intervals (Medium)

### **链接**：
题目：https://leetcode.com/problems/merge-intervals  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一组区间，要求合并其中相互重叠的并输出。

### **分析**  
1. 直接模拟：时间复杂度O(n2)，空间复杂度O(n)。
	- 依次将输入的区间推入结果，每次推入遍历结果中已存在的区间，合并重合的。
	
2. 排序左值：时间复杂度O(nlogn), 空间复杂度O(n)。
	- 将区间按左值大小排序，然后再依次比较相邻区间并推入结果。

3. 分别排序左右值：时间复杂度O(nlogn), 空间复杂度O(n)。
	- 将区间左右值分开放入两个数组排序。
	- 比较排序后的左值和右值构成区间
