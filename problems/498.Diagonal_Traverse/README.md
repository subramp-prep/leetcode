## 498. Diagonal Traverse (Medium)

### **链接**：
题目：https://leetcode.com/problems/diagonal-traverse  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一矩阵，要求按对角线顺序输出其所有值。


### **分析**  
题目类别(Tags)：  
最优复杂度(Complexity)：O(mn)  
 
复杂度不可能小于O(mn)，因为要遍历全部矩阵。 
1. 可以模拟遍历过程，出界即换方向。
2. 也可研究序号规律，分奇偶情况

作者: Yin