from typing import ClassVar

from solutions.vendor.ch06.empty import Empty


class ArrayDeque:
    _DEFAULT_CAPACITY: ClassVar[int] = 10

    _data: list
    _size: int
    _first: int
    _last: int

    def __init__(self):
        self._data = [None] * ArrayDeque._DEFAULT_CAPACITY
        self._size = 0
        self._first = 0
        self._last = len(self._data) - 1

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) == 0

    def _resize(self, cap):
        new_data = [None] * cap
        first_size = self._size // 2
        last_size = self._size - first_size
        for i in range(first_size - 1, -last_size - 1, -1):
            new_data[i] = self._data[(self._first - i + first_size - 2) % len(self._data)]
        self._first = first_size
        self._last = len(new_data) - (last_size + 1)
        self._data = new_data

    def add_first(self, e):
        if len(self) == len(self._data):
            self._resize(2 * len(self))
        self._data[self._first] = e
        self._first += 1
        self._size += 1

    def add_last(self, e):
        if len(self) == len(self._data):
            self._resize(2 * len(self))
        self._data[self._last] = e
        self._last -= 1
        self._size += 1

    def delete_first(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        if len(self._data) // 4 > len(self) > ArrayDeque._DEFAULT_CAPACITY:
            self._resize(max(ArrayDeque._DEFAULT_CAPACITY, len(self._data) // 2))
        self._first = (self._first - 1) % len(self._data)
        result = self._data[self._first]
        self._data[self._first] = None
        self._size -= 1
        return result

    def first(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        return self._data[(self._first - 1) % len(self._data)]

    def delete_last(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        if len(self._data) // 4 > len(self) > ArrayDeque._DEFAULT_CAPACITY:
            self._resize(max(ArrayDeque._DEFAULT_CAPACITY, len(self._data) // 2))
        self._last = (self._last + 1) % len(self._data)
        result = self._data[self._last]
        self._data[self._last] = None
        self._size -= 1
        return result

    def last(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        return self._data[(self._last + 1) % len(self._data)]

    def __str__(self):
        result: list[str] = [""] * len(self)
        for i in range(len(self)):
            result[i] = str(self._data[(self._first - 1 - i) % len(self._data)])

        return "[{}]".format(", ".join(result))
