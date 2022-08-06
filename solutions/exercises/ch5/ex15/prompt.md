Consider an implementation of a dynamic array, but instead of copying
the elements into an array of double the size (that is, from $N$ to $2N$) when
its capacity is reached, we copy the elements into an array with $\lceil \frac{N}{4} \rceil$
additional cells, going from capacity $N$ to capacity $N + \lceil \frac{N}{4} \rceil$. Prove that
performing a sequence of $n$ append operations still runs in $O(n)$ time in this case.