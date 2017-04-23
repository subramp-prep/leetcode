Short Ruby / Python / Java / C++ | LeetCode Discuss
============================
**Author:**  StefanPochmann
**Reputation:**  14940 

<p>Just Eulerian path. Greedy DFS, building the route backwards when retreating.</p>
<p>More explanation and example under the codes.</p>
<p>Iterative versions inspired by <a href="https://leetcode.com/discuss/84706/share-solution-java-greedy-stack-15ms-with-explanation" rel="nofollow">fangyang</a> (I had only thought of recursion, d'oh).</p>
<hr/>
<p><strong>Ruby</strong></p>
<pre><code>def find_itinerary(tickets)
  tickets = tickets.sort.reverse.group_by(&amp;:first)
  route = []
  visit = -&gt; airport {
    visit[tickets[airport].pop()[1]] while (tickets[airport] || []).any?
    route &lt;&lt; airport
  }
  visit["JFK"]
  route.reverse
end
</code></pre>
<p>Iterative version:</p>
<pre><code>def find_itinerary(tickets)
  tickets = tickets.sort.reverse.group_by(&amp;:first)
  route, stack = [], ["JFK"]
  while stack.any?
    stack &lt;&lt; tickets[stack[-1]].pop()[1] while (tickets[stack[-1]] || []).any?
    route &lt;&lt; stack.pop()
  end
  route.reverse
end
</code></pre>
<hr/>
<p><strong>Python</strong></p>
<pre><code>def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route = []
    def visit(airport):
        while targets[airport]:
            visit(targets[airport].pop())
        route.append(airport)
    visit('JFK')
    return route[::-1]
</code></pre>
<p>Iterative version:</p>
<pre><code>def findItinerary(self, tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
    return route[::-1]
</code></pre>
<hr/>
<p><strong>Java</strong></p>
<pre><code>public List&lt;String&gt; findItinerary(String[][] tickets) {
    for (String[] ticket : tickets)
        targets.computeIfAbsent(ticket[0], k -&gt; new PriorityQueue()).add(ticket[1]);
    visit("JFK");
    return route;
}

Map&lt;String, PriorityQueue&lt;String&gt;&gt; targets = new HashMap&lt;&gt;();
List&lt;String&gt; route = new LinkedList();

void visit(String airport) {
    while(targets.containsKey(airport) &amp;&amp; !targets.get(airport).isEmpty())
        visit(targets.get(airport).poll());
    route.add(0, airport);
}
</code></pre>
<p>Iterative version:</p>
<pre><code>public List&lt;String&gt; findItinerary(String[][] tickets) {
    Map&lt;String, PriorityQueue&lt;String&gt;&gt; targets = new HashMap&lt;&gt;();
    for (String[] ticket : tickets)
        targets.computeIfAbsent(ticket[0], k -&gt; new PriorityQueue()).add(ticket[1]);
    List&lt;String&gt; route = new LinkedList();
    Stack&lt;String&gt; stack = new Stack&lt;&gt;();
    stack.push("JFK");
    while (!stack.empty()) {
        while (targets.containsKey(stack.peek()) &amp;&amp; !targets.get(stack.peek()).isEmpty())
            stack.push(targets.get(stack.peek()).poll());
        route.add(0, stack.pop());
    }
    return route;
}
</code></pre>
<hr/>
<p><strong>C++</strong></p>
<pre><code>vector&lt;string&gt; findItinerary(vector&lt;pair&lt;string, string&gt;&gt; tickets) {
    for (auto ticket : tickets)
        targets[ticket.first].insert(ticket.second);
    visit("JFK");
    return vector&lt;string&gt;(route.rbegin(), route.rend());
}

map&lt;string, multiset&lt;string&gt;&gt; targets;
vector&lt;string&gt; route;

void visit(string airport) {
    while (targets[airport].size()) {
        string next = *targets[airport].begin();
        targets[airport].erase(targets[airport].begin());
        visit(next);
    }
    route.push_back(airport);
}
</code></pre>
<hr/>
<p><strong>Explanation</strong></p>
<p>First keep going forward until you get stuck. That's a good main path already. Remaining tickets form cycles which are found on the way back and get merged into that main path. By writing down the path backwards when retreating from recursion, merging the cycles into the main path is easy - the end part of the path has already been written, the start part of the path hasn't been written yet, so just write down the cycle now and then keep backwards-writing the path.</p>
<p>Example:</p>
<p><img src="http://www.stefan-pochmann.info/misc/reconstruct-itinerary.png" alt="enter image description here" class="img-responsive img-markdown"/></p>
<p>From JFK we first visit JFK -&gt; A -&gt; C -&gt; D -&gt; A. There we're stuck, so we write down A as the end of the route and retreat back to D. There we see the unused ticket to B and follow it: D -&gt; B -&gt; C -&gt; JFK -&gt; D. Then we're stuck again, retreat and write down the airports while doing so: Write down D before the already written A, then JFK before the D, etc. When we're back from our cycle at D, the written route is D -&gt; B -&gt; C -&gt; JFK -&gt; D -&gt; A. Then we retreat further along the original path, prepending C, A and finally JFK to the route, ending up with the route JFK -&gt; A -&gt; C -&gt; D -&gt; B -&gt; C -&gt; JFK -&gt; D -&gt; A.</p> 

Ref: https://discuss.leetcode.com/topic/36370
