## 530. Minimum Absolute Difference in BST (Easy)

### **链接**：
题目：https://leetcode.com/problems/minimum-absolute-difference-in-bst  
题解：https://github.com/JianghanLi/LeetCode

### **题意**
给一二叉搜索树，求两节点差的最小值。


### **分析**  
题目类别(Tags)：Binary Search Tree  
最优复杂度(Complexity)：时间复杂度O(n)，空间复杂度O(h)  

1. 中序遍历（In-order Traversal）：时间复杂度O(n)，空间复杂度O(h)
	- 二叉搜索树中序遍历会从小到大依次遍历树中节点，所以此题中序遍历求相邻两值的差即可