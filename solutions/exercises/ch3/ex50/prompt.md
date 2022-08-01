Let $p(x)$ be a polynomial of degree $n$, that is, $p(x) = \sum^n_{i=0} a_ix^i$.
(a) Describe a simple $O(n^2)$-time algorithm for computing $p(x)$.
(b) Describe an $O(n\log n)$-time algorithm for computing $p(x)$, based upon
a more efficient calculation of $x^i$.
(c) Now consider a rewriting of $p(x)$ as
$p(x) = a_0 +x(a_1 +x(a_2 +x(a_3 +···+x(a_{n−1} + xa_n)···)))$,
which is known as **Horner’s method**. Using the big-Oh notation, characterize the number of arithmetic operations this
method executes.
