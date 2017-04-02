## 122. Best Time to Buy and Sell Stock II (Medium)

### **链接**：
题目：https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/  
代码(github)：https://github.com/JianghanLi/LeetCode

### **题意**：
给一个数组，`prices[i]` 表示第 i 天的交易值，也就是你在这天买入或卖出的交易值。  
你可以买入及卖出多轮，不过你一个时间只能拥有一个股票，求最大盈利。

### **分析**：
  
1. 贪心法：时间复杂度O(n)，空间复杂度O(1)。
	- 同一天可以先卖出再买入。贪心法就行了，考虑 [1, 2, 3]，你可以 [-1, +2-2, +3]，跟 [-1, +3] 是一样的，也就是说只要比前一天多，你就可以在前一天买入，接下去一天卖出，这样稳赚不赔。

2. 模拟法：时间复杂度O(n)，空间复杂度O(1)。
	- 直接模拟也可做，思路就是低谷买入，高峰卖出。