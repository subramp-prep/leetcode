My concise JAVA solution based on memorized DFS | LeetCode Discuss
============================
**Author:**  ChengZhang
**Reputation:**  972 

<p><strong>Explanation</strong></p>
<p>Using DFS directly will lead to TLE, so I just used HashMap to save the previous results to prune duplicated branches, as the following:</p>
<pre><code>public List&lt;String&gt; wordBreak(String s, Set&lt;String&gt; wordDict) {
    return DFS(s, wordDict, new HashMap&lt;String, LinkedList&lt;String&gt;&gt;());
}       

// DFS function returns an array including all substrings derived from s.
List&lt;String&gt; DFS(String s, Set&lt;String&gt; wordDict, HashMap&lt;String, LinkedList&lt;String&gt;&gt;map) {
    if (map.containsKey(s)) 
        return map.get(s);
        
    LinkedList&lt;String&gt;res = new LinkedList&lt;String&gt;();     
    if (s.length() == 0) {
        res.add("");
        return res;
    }               
    for (String word : wordDict) {
        if (s.startsWith(word)) {
            List&lt;String&gt;sublist = DFS(s.substring(word.length()), wordDict, map);
            for (String sub : sublist) 
                res.add(word + (sub.isEmpty() ? "" : " ") + sub);               
        }
    }       
    map.put(s, res);
    return res;
}</code></pre> 

Ref: https://discuss.leetcode.com/topic/27855
