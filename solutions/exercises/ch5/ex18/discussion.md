The worst case in for this scheme is to append until a doubling is triggered and then pop until a halving is triggered.
However, we already proved in Ex 5.17 that such a sequence of length $n$ will take $O(n)$ time. Since the worst
sequence of $n$ append and/or pop operations will take $O(n)$ time, we can conclude that any sequence of $n$ append
and/or pop operations will take $O(n)$ time.