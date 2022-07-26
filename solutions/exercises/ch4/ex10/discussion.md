<pre><code>
<b>Algorithm</b> LgFloor(n):
    <i><b>Input:</b></i> An integer n
    <i><b>Output:</b></i> The "integer part" (i.e. floor) of lg(n)
    <b>if</b> n == 1 <b>then</b>
        <b>return</b> 0
    <b>else</b>
        <b>return</b> 1 + LgFloor(n//2)
</code></pre>