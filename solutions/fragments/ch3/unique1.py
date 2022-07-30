# This is the unique1 algorithm of section 3.3.3 that is referenced in the exercises.


def unique1(S):
    """Return True if there are no duplicate elements in sequence S."""
    for j in range(len(S)):
        for k in range(j + 1, len(S)):
            if S[j] == S[k]:
                return False            # found duplicate pair
    return True                         # if we reach this, elements were unique
