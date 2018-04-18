
697.Degree_of_an_Array
----------------------------------------------
Problem: https://leetcode.com/problems/degree-of-an-array
Solution: https://github.com/JianghanLi/LeetCode/problems/697.Degree_of_an_Array
Discuss: https://leetcode.com/problems/degree-of-an-array/discuss/124317/C++JavaPython-one-pass-and-O(M)-space


###**Discuss**：
I hardly find the reason to give a second pass, especilly for C++ and Java.
Also the problem can be easily solved by only O(M) space, where M is the size of numbers set.
So I write this post to let you forget those multi-pass and O(N) space solutions.


```
loop only once on array {
    record the index of first occureence;
    update number counter;
    update result;
}
return result;
```