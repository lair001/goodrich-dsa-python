# This is the prefix_average2 algorithm of section 3.3.3 that is referenced in the exercises.


def prefix_average3(S):
    """Return list such that, for all j, A[j] equals average of S[0], ..., S[j]."""
    n = len(S)
    A = [0] * n                        # create new list of n zeros
    total = 0                          # compute prefix sum as S[0] + S[1] + ...
    for j in range(n):
        total += S[j]                  # update prefix sum to include S[j]
        A[j] = total / (j+1)           # compute average based on current sum
    return A