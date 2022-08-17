from solutions.vendor.ch06.empty import Empty


class LeakyStack:
    _data: list
    _size: int
    _top: int

    def __init__(self, maxlen: int = 8):
        self._data = [None] * maxlen
        self._top = 0
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) < 1

    def push(self, e):
        self._data[self._top] = e
        self._top = (self._top + 1) % len(self._data)
        if self._size < len(self._data):
            self._size += 1

    def pop(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        self._top = (self._top - 1) % len(self._data)
        result = self._data[self._top]
        self._data[self._top] = None
        self._size -= 1
        return result

    def top(self):
        if self.is_empty():
            raise Empty("Stack is empty!")
        return self._data[(self._top - 1) % len(self._data)]

    def __str__(self):
        return "[{}]".format(", ".join(map(str, (self._data[(self._top - len(self) + i) % len(self._data)]
                                                 for i in range(len(self))))))

