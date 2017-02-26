## 071.Simplify Path (Medium)  
  
### **链接**：  
题目：https://leetcode.com/problems/simplify-path/
代码(github)：https://github.com/JianghanLi/LeetCode  
  
### **题意**：  
简化Unix路径。
  
### **分析**：
建立stack，直接模拟即可。
P.S.
	- 取出两个/之间的路径信息，C++中可以用stringstream
	- 也可以用别的更优化的数据结构来替代stack