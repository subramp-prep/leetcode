## 148.Insertion Sort List (Medium)

### **链接**：
题目：https://leetcode.com/problems/insertion-sort-list/
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把一个链表升序排列。要求使用插入算法

### **分析**：
直接使用插入算法即可。可以不创建新node，让空间复杂度为O(1)。
链表相对于数组使用这个算法有一点优势，可直接插入node，不需要位移。数组在寻找插入点时可以使用二分法，但链表不可以。