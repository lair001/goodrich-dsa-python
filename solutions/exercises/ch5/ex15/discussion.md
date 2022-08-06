The cyber-dollar argument employed by the authors is just a gimmick to express three axioms. The first is that cost
of increasing the size of the array grows linearly with the size of the array. This follows from the fact that a new
array is allocated whose size depends linearly on the of the old array and that the elements of the old array are
copied to the new array. The second is that if the number of operations since the last size increase also increases
linearly with the size of the array, then amortized cost per operation is a fixed constants. The third axiom is that the
cost of the operation is constant when an array resizing does not occur. If all of these axioms hold, then we can
conclude that the total time to perform n operations is $O(n)$.

If you understand the above, then its obvious that the resizing scheme presented in this problem results in $n$ append
operations running in $O(n)$ time. Nonetheless, I will still present a "formal cyber-dollar" analysis.

Let us take the cost of increasing the size of the array from $N$ to $N + \lceil \frac{N}{4} \rceil$ to be $k$
cyber-dollars. Therefore, we must save $k$ cyber-dollars over the $\frac{N}{5}$ operations since the last resizing.
I.e. we must save 5 cyber-dollars per operation. Each operation that does not result in a resizing costs a constant
amount. Let's take this amount to be 1 cyber-dollar. We must charge a total of 6 cyber-dollars per append operation,
which is a constant amount. Hence, we can conclude that $n$ append operations still runs in $O(n)$ time.
