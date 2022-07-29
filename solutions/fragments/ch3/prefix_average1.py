# This is the prefix_average1 algorithm of section 3.3.3 that is referenced in the exercises.


def prefix_average1(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                          # create new list of n zeros
    for j in range(n):
        total = 0                        # begin computing S[0] + ... + S[j]
        for i in range(j + 1):
            total += S[i]
        A[j] = total / (j+1)             # record the
    return A