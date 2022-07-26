<pre><code>
<b>Algorithm</b> Product(m, n):
    <i><b>Input:</b></i> Integers m and n such that m >= n
    <i><b>Output:</b></i> The product of m and n
    <b>if</b> n == 0 <b>then</b>
        <b>return</b> 0
    <b>else if</b> n == 1 <b>then</b>
        <b>return</b> m
    <b>else</b>
        <b>return</b> m + Product(m, n-1)
</code></pre>