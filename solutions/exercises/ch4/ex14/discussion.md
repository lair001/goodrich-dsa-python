<pre><code>
<b>Algorithm</b> TowerOfHanoi(A, B, C, n):
    <i><b>Input:</b></i>  Target stack A, storage stack B, source stack C, and integer n for the number of disks to
            move from C to A.
    <i><b>Output:</b></i> An updated state where n disks have been moved from C to A without violating the rules of
            the game.
    <b>if</b> n > 0 <b>then</b>
        TowerOfHanoi(B, A, C, n - 1)
        Move remaining disk from C to A
        TowerOfHanoi(A, C, B, n - 1)
</code></pre>

The script for this algorithm can be found in the solution for ex 4.26