Since Proposition 5.1 already proves that a sequence of $n$ append operations takes $O(n)$ time, we need only
prove that a sequence of $n$ pop operations also takes $O(n)$ time.

The first array shrinking could be amortized over $\frac{n}{2}$ to $\frac{3n}{2}$ pop operations depending on
whether the append operations end at a doubling, or at capacity, or somewhere in between. However, all subsequent
shrinkings will be amortized over $\frac{n'}{2}$ where $n'$ is the new size after the last shrinking. Therefore,
we will amortize over $\frac{n}{2}$ pop operations to give an upperbound.

We can see that the cost of shrinking the array has a linear relationship to $n$ from the fact that the size of the
new array has a linear relationship with $n$ and the fact that the number of elements we must copy to the new array has
a linear relationship with $n$.  Let us set this cost to $an$ cyber-dollars.  We must save this amount over $\frac{n}{2}$
pop operations. I.e. we must save $2a$ cyber-dollars per pop operation. A pop operation that does not trigger a resizing
is a constant cost operation. We'll denote this cost as $b$ cyber-dollars. Therefore, we must charge $2a + b$
cyber-dollars per pop operation. Since this amortized cost is constant, we can conclude that $n$ pop operations take
$O(n)$ time.
