## 006.ZigZag_Conversion (Easy)

### **链接**：
题目：https://leetcode.com/problems/zigzag-conversion/  
代码(github)：https://github.com/JianghanLi/LeetCode  

### **题意**：
把一个字符串按横写的折线排列。  

### **分析**：
1. 直接模拟就行了。
2. 也可以依据行列规律直接算出某位置在原string的位置。
   每行相邻两元素之间的差可以依照行列位置算出。难点是判断什么时候换行。
   空间复杂度为O(n);
	1      7         13
	 2    6  8     12  14
	  3  5    9  11      15
	   4       10
