## 238. Product of Array Except Self (Medium)

### **链接**：
题目：https://leetcode.com/problems/product-of-array-except-self/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
把一个数组中的每个数 替换为 这个数组中除了它自身的其它数的积。

### **分析**：

1. 最暴力的是直接在每个位置计算其它数的积，时间复杂度 O(n*n)。
2. 先算出所有的数的积，再去用除法求出解，要注意数组里可能会有 0，一个 0 和多个 0 的情况是不一样的。空间复杂度是 O(1)，时间是 O(n)。
3. 其实就是算每个位置上左边的数和右边的数的积，所以可以开数组预处理出每个位置左右两边的积，然后再相乘就行了。实际做的时候只要用一个数组记录一边就行了，另一边可以一边算一边得出解来。

