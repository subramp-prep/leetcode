## 172. Factorial Trailing Zeroes (Easy)

### **链接**：
题目：https://leetcode.com/problems/factorial-trailing-zeroes/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：

求n!末尾有几个0。要求时间复杂度为对数。

### **分析**：

显然，求n!末尾0的数目，等价于其中5出现的数目。  
计算5出现数目的方法，在n到n/5之间，5出现的次数是n/5，所以有：  
[n/5] + [n/5/5] + [n/5/5/5] + ...  
根据这个思路，用迭代和递归法均可。