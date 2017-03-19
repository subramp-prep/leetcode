<div class="container">
<div class="row">
<div class="col-md-12">
<div class="question-title clearfix">
<h3>527. Word Abbreviation</h3>
<div class="pull-right top-buttons">
<div class="btn-group right-pad">
<a class="btn btn-default" href="https://leetcode.com/contest/leetcode-weekly-contest-23/problems/word-abbreviation/submissions/">My Submissions</a>
<a class="btn btn-success" href="https://leetcode.com/contest/leetcode-weekly-contest-23/">Back To Contest</a>
</div>
</div>
</div>
<div class="row col-md-12">

</div>
<div class="row">
<div class="col-md-12">
<div class="question-info text-info">
<ul>


<li>User Accepted: <strong>135</strong></li>

<li>User Tried: <strong>283</strong></li>


<li>Total Accepted: <strong>139</strong></li>

<li>Total Submissions: <strong>642</strong></li>
<li>Difficulty: <strong>Hard</strong></li>
</ul>
</div>
<div class="question-content">
<p></p><p>Given an array of n distinct non-empty strings, you need to generate <b>minimal</b> possible abbreviations for every word following rules below.</p>

<ol>
<li>Begin with the first character and then the number of characters abbreviated, which followed by the last character.</li>
<li>If there are any conflict, that is more than one words share the same abbreviation, a longer prefix is used instead of only the first character until making the map from word to abbreviation become unique. In other words, a final abbreviation cannot map to more than one original words.</li>
<li> If the abbreviation doesn't make the word shorter, then keep it as original.</li>
</ol>

<p><b>Example:</b><br>
</p><pre><b>Input:</b> ["like", "god", "internal", "me", "internet", "interval", "intension", "face", "intrusion"]
<b>Output:</b> ["l2e","god","internal","me","i6t","interval","inte4n","f2e","intr4n"]
</pre>
<p></p>


<b>Note:</b>
<ol>
<li> Both n and the length of each word will not exceed 400.</li>
<li> The length of each word is greater than 1.</li>
<li> The words consist of lowercase English letters only.</li>
<li> The return answers should be <b>in the same order</b> as the original array.</li>
</ol><p></p>
</div>
</div>
</div>
</div>
</div>

<p class="action">

<a class="btn btn-success btn-pad right-pad" href="https://discuss.leetcode.com/category/677" target="_blank">Discuss</a>




</p>

<hr>
</div>