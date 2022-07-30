# This is the unique3 algorithm of section 4.3 that is referenced in the exercises.


def unique3(S):
    return _unique3(S, 0, len(S))


def _unique3(S, start, stop):
    """Return True if there are no duplicate elements in slice S[start:stop]."""
    if stop - start <= 1:
        return True  # at most one item
    elif not _unique3(S, start, stop - 1):
        return False  # first part has duplicate
    elif not _unique3(S, start + 1, stop):
        return False  # second part has duplicate
    else:
        return S[start] != S[stop - 1]  # do first and last differ?
