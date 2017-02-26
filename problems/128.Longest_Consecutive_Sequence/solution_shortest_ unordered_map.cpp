class Solution {
public:
  int longestConsecutive(vector<int> &num) {
    unordered_map<int, int> m;
    int r = 0;
    for (int i : num) {
      if (m[i]) continue;
      r = max(r, m[i] = m[i + m[i + 1]] = m[i - m[i - 1]] = m[i + 1] + m[i - 1] + 1);
    }
    return r;
  }
};


// https://discuss.leetcode.com/topic/5333/possibly-shortest-cpp-solution-only-6-lines/11
// use a hash map to store boundary information of consecutive sequence
//for each element; there 4 cases when a new element i reached:

// neither i+1 nor i-1 has been seen: m[i]=1;
// both i+1 and i-1 have been seen: extend m[i+m[i+1]] and m[i-m[i-1]] to each other;
// only i+1 has been seen: extend m[i+m[i+1]] and m[i] to each other;
// only i-1 has been seen: extend m[i-m[i-1]] and m[i] to each other.

// the default allocator initializes int to 0. you can see this:
// http://www.cplusplus.com/reference/unordered_map/unordered_map/operator[]/
// and this:
// http://stackoverflow.com/questions/9584660/does-the-default-allocator-zeroize-int


// Attition：
// Can‘t  use m.count(i) instead of m[i].
// It should skip only if m[i] > 0, not if m[i] existed.
// If you are getting a value from the map with a new key,
//then it will insert an default-constructed value into the map. If m[1+1] doesn't exist, it will be 0.

// 思路是在链子左右两端纪录是链子长度，然后不断更新。
// 遍历每个数时候检查它左右两边的数 然后把这个数，以及它所在链子左右两端，一起赋值为找到链子的长度。
// CPP里max函数可以有赋值语句，所以看起来特别短。