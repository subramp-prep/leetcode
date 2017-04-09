2 C++ Solutions with Explanations | LeetCode Discuss
============================
**Author:**  jianchao.li.fighter
**Reputation:**  4320 

<hr/>
<p><strong>Hash Table</strong></p>
<p>This idea uses a hash table to record the times of appearances of each letter in the two strings <code>s</code> and <code>t</code>. For each letter in <code>s</code>, it increases the counter by <code>1</code> while for each letter in <code>t</code>, it decreases the counter by <code>1</code>. Finally, all the counters will be <code>0</code> if they two are anagrams of each other.</p>
<p>The first implementation uses the built-in <code>unordered_map</code> and takes 36 ms.</p>
<pre><code>class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        unordered_map&lt;char, int&gt; counts;
        for (int i = 0; i &lt; n; i++) {
            counts[s[i]]++;
            counts[t[i]]--;
        }
        for (auto count : counts)
            if (count.second) return false;
        return true;
    }
};
</code></pre>
<p>Since the problem statement says that "the string contains only lowercase alphabets", we can simply use an array to simulate the <code>unordered_map</code> and speed up the code. The following implementation takes 12 ms.</p>
<pre><code>class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.length() != t.length()) return false;
        int n = s.length();
        int counts[26] = {0};
        for (int i = 0; i &lt; n; i++) { 
            counts[s[i] - 'a']++;
            counts[t[i] - 'a']--;
        }
        for (int i = 0; i &lt; 26; i++)
            if (counts[i]) return false;
        return true;
    }
};
</code></pre>
<hr/>
<p><strong>Sorting</strong></p>
<p>For two anagrams, once they are sorted in a fixed order, they will become the same. This code is much shorter (this idea can be done in just 1 line using Python as <a href="https://leetcode.com/discuss/49372/python-1-line-solution-88ms" rel="nofollow">here</a>). However, it takes much longer time --- 76 ms in C++.</p>
<pre><code>class Solution {
public:
    bool isAnagram(string s, string t) { 
        sort(s.begin(), s.end());
        sort(t.begin(), t.end());
        return s == t; 
    }
};
</code></pre> 

Ref: https://discuss.leetcode.com/topic/20303
