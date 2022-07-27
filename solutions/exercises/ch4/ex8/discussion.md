The memory complexity of Isabel's summing algorithm is $\Theta(n)$. During a given run of her algorithm, the highest
memory consumption is when she makes an array of size $\frac{n}{2}$ during the first call.

The number of recursive calls is proportional to $lg(n)$ (similar to binary search) but the array she is iterating over
halves in size each time. Therefore, the total number of elements she's iterating over is proportional to
$n\log_{2}(n)({\frac{1}{2}}^0 + {\frac{1}{2}}^1 + {\frac{1}{2}}^2 + {\frac{1}{2}}^3 + ... + {\frac{1}{2}}^{\log_{2}(n)})$.
Hence, the runtime complexity of her algorithm is $\Theta(n{\log_{2}}^2(n))$.
