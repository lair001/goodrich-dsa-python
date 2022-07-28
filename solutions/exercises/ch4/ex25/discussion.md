The prompt gives the answer away. This works because the number of consecutive zeroes at the end of an increasing
binary number happens to follow the same pattern as the length of ticks within an interval of a binary ruler. However,
it is unlikely that I would make this observation on my own.

How could we try to develop an intuition about this sort of problem? Well, as the prompt points out, the number of
ticks within any given interval in a ruler is equal to $2^{c} - 1$, where $c$ is the length of the central tick.  So
let us consider the smallest nontrivial interval: an interval with $c = 2$. The binary representation
of the integers 0, 1, and 2 are 00, 10, and 01.  Things check out so far and given the repeating nature of binary
digits, much like the repeating nature of the tick lengths, you might be tempted to check out $c = 3$ and check out the
pattern of the three bit numbers less than $2^{3}$: 000, 100, 010, 110, 001, 101, 011. So we've just shown that the
relation works for $c = 2$ and $c = 3$. Note that it is trivially true for $c = 1$: 0.

Since we have some base cases, if we can work out a recurrence relation, then we can do a proof by induction. Suppose
that the relation holds for $c$ and consider $c+1$.  Then the length of the new interval is $2^{c+1} - 1$.  We merely
added a bit to our set of binary numbers.  Every element of the previous set is in the new set and we construct the
new members by prepending a 1 to each of the previous elements.  Hence, the pattern of consecutive ending ones continues
to match increasingly larger English ruler intervals.
