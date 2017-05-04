## 541. Reverse String II (Easy)

### **链接**：
题目：https://leetcode.com/problems/reverse-string-ii  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一个字符串和一个整数k，要求反转字符串中每2k个字符的前k个，若最后剩下字符不足k个，全部反转


### **分析**  
1. 直接模拟即可：时间复杂度O(n^2)，空间复杂度O(1)。
	- 在原字符串的基础上反转字符串：头尾开始向中间遍历的双指针，值相互交换