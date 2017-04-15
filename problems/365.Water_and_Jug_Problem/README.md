## 365. Water and Jug Problem (Medium)

### **链接**：
题目：https://leetcode.com/problems/water-and-jug-problem
题解：https://github.com/JianghanLi/LeetCode

### **题意**
小奥倒水问题。直观想法就是求一下最大公约数。



### **分析**
题目类别(Tags)：Math
最优复杂度(Complexity)：O(NlogN)

数学简单证明，对于能倒出来的结果，对于不定方程n*x-m*y一定有解。
倒水方案，就是求此不定方程解的过程
对于x,y互质的情况，(0-y)*x％y一定可以得到0-y的一个排列。
更为有趣直观的讲解，可以参考
https://www.youtube.com/watch?v=0Oef3MHYEC0

