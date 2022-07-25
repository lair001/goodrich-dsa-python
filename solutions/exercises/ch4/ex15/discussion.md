For our base case, we observe that the null set is only subset when $n = 0$.

For our recurrence relation, suppose that we know all of the subsets for $n - 1$.
Then the subsets for $n$ include all the subsets for $n - 1$ plus a new group of
subsets derived by appending the nth element to every subset for $n - 1$.

Unfortunately, this recurrence relation means that the number of subsets double
every time you add an element. This means there is no algorithm that will solve
this problem in better than $\theta(2^n)$ time and memory complexity since we must
visit and store every possible subset at least once.
