# This is the prefix_average2 algorithm of section 3.3.3 that is referenced in the exercises.


def prefix_average2(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                          # create new list of n zeros
    for j in range(n):
        A[j] = sum(S[0:j+1]) / (j+1)     # record the average
    return A