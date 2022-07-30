# This is the unique2 algorithm of section 3.3.3 that is referenced in the exercises.


def unique2(S):
    """Return True if there are no duplicate elements in sequence S."""
    temp = sorted(S)                # create a sorted copy of S
    for j in range(1, len(temp)):
        if S[j - 1] == S[j]:
            return False            # found duplicate pair
    return True                     # if we reach this, elements were unique
