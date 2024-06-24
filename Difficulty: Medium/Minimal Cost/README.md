<h2><a href="https://www.geeksforgeeks.org/problems/minimal-cost/1?utm_source=youtube&utm_medium=collab_striver_ytdescription&utm_campaign=minimal-cost">Minimal Cost</a></h2><h3>Difficulty Level : Difficulty: Medium</h3><hr><div class="problems_problem_content__Xm_eO" bis_skin_checked="1"><p><span style="font-size: 18px;">There are n stones and an array of heights&nbsp;and Geek is standing at stone 1 and can&nbsp;jump to one of the following: Stone i+1, i+2, ... i+k stone and cost will be [h<sub>i</sub>-h<sub>j</sub>] is incurred, where j is the stone to land on. Find the minimum possible total cost incurred before the Geek reaches Stone n.</span></p>
<pre><span style="font-size: 18px;"><strong>Examples :</strong>
<strong>Input: </strong>n = 5, k = 3 heights = {10, 30, 40, 50, 20}
<strong>Output: </strong>30
<strong>Explanation: </strong>Geek will follow the path 1-&gt;2-&gt;5, the total cost would be | 10-30| + |30-20| = 30, which is minimum</span></pre>
<pre><span style="font-size: 18px;"><strong>Input: </strong>n = 3, k = 1 heights = {10,20,10}
<strong>Output: </strong>20
<strong>Explanation: </strong></span><span style="font-size: 20px;">Geek will follow the path 1-&gt;2-&gt;3, the total cost would be |10 - 20| + |20 - 10| = 20.</span>
</pre>
<p><strong><span style="font-size: 18px;">Your Task:</span></strong><br><span style="font-size: 18px;">You don't need to read input or print anything. Your task is to complete the function <strong>minimizeCost()&nbsp;</strong>which takes the array&nbsp;<strong>height</strong>, and integer <strong>n, </strong>and integer k&nbsp;and returns the minimum energy that is lost.</span></p>
<p><span style="font-size: 18px;"><strong>Expected Time Complexity</strong>: O(n*k)<br><strong>Expected Space Complexity</strong>: O(n)</span></p>
<p><span style="font-size: 18px;"><strong>Constraint:</strong><br>2 &lt;= n &lt;= 10<sup>5</sup><br>1 &lt;= k &lt;= 100<br>1 &lt;= heights[i] &lt;= 10<sup>4</sup></span></p></div><br><p><span style=font-size:18px><strong>Topic Tags : </strong><br><code>Dynamic Programming</code>&nbsp;<code>Arrays</code>&nbsp;<code>Data Structures</code>&nbsp;<code>Algorithms</code>&nbsp;