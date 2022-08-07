The worst possible sequence for this resizing scheme would be starting right after a doubling, pop twice to trigger
a halving and then append twice to trigger another doubling. Repeat as many times as desired. Under this sequence,
we must amortize the linear cost doubling and halving operations over a constant number of append and pop operations.
This means that the amortized cost per append or pop operation is linear. Hence, a sequence of this sort comprising
$n$ append and pop operations will take $\Omega(n^2)$ time.
