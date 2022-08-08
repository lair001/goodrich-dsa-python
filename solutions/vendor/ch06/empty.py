# For whatever reason, this exception was not included in the booktsite's code source files for ch 6 even though
# ArrayQueue and ArrayStack link to it. This implementation is copied from Code Fragment 6.1 on page 232 of the book.

class Empty(Exception):
    """Error attempting to access an element from an empty container."""
    pass
