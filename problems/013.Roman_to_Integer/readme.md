## 013.Roman_to_Integer (Easy)

### **链接**：
题目：https://leetcode.com/problems/roman-to-integer/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把罗马数转为十进制。

### **分析**：
跟 [012. Integer to Roman (Medium)](http://blog.csdn.net/hcbbt/article/details/44026099) 一样，只要知道转化规则就行了。

所有的值都在罗马数字中体现，建立hashtable取值加减就可以了。
观察规则则是，某字母的数值比右边的数值小时减去它，否则加上。