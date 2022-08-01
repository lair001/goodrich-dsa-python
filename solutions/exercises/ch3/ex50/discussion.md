Let us characterize the number of arithmetic operations that **Horner's method**. The body of our for loop has
2 explicit multiplications and 1 explicit addition.

If you are not familiar with pointers, you may not be aware that that array accesses also involve arithmetic.
Basically, a pointer to an array actually points to the element at index 0. If you want to access an element at a
different index, you add index * element_size to the pointer. Hence, each array access to an index other than zero
adds two arithmetic operations to our total.

Our only loop runs $n$ times where $n = d + 1$ and $d$ is the degree of our polynomial. For $n - 1$ iterations, we
have 2 explicit multiplications, 1 explicit addition and 1 multiplication and 1 addition from the array access for a
total of $5 (n-1)$ arithmetic operations. The first iteration of the loop only executes 1 explicit multiplication and
1 explicit addition. Therefore, we have a total of $5n-3$ arithmetic operations. Hence, **Horner's method** is $\Theta(n)$.
