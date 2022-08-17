from typing import ClassVar

from solutions.vendor.ch06.empty import Empty


class CollectionsDeque:
    _DEFAULT_CAPACITY: ClassVar[int] = 4

    _data: list
    _size: int
    _left: int
    _right: int
    _maxlen: int | None

    def __init__(self, maxlen: int | None = None):
        self._data = [None] * (CollectionsDeque._DEFAULT_CAPACITY if maxlen is None else maxlen)
        self._size = 0
        self._left = 0
        self._right = len(self._data) - 1
        self._maxlen = maxlen

    def __len__(self):
        return self._size

    def is_empty(self):
        return len(self) < 1

    def _resize(self, cap):
        new_data = [None] * cap
        first_size = self._size // 2
        last_size = self._size - first_size
        for i in range(first_size - 1, -last_size - 1, -1):
            new_data[i] = self._data[(self._left + i - first_size) % len(self._data)]
        self._left = first_size
        self._right = len(new_data) - (last_size + 1)
        self._data = new_data

    def appendleft(self, e):
        if self._maxlen is None and len(self) == len(self._data):
            self._resize(2 * len(self))
        self._data[self._left] = e
        self._left += 1
        self._size += 1

    def append(self, e):
        if self._maxlen is None and len(self) == len(self._data):
            self._resize(2 * len(self))
        self._data[self._right] = e
        self._right -= 1
        self._size += 1

    def popleft(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        if self._maxlen is None and len(self._data) // 4 > len(self) > CollectionsDeque._DEFAULT_CAPACITY:
            self._resize(max(CollectionsDeque._DEFAULT_CAPACITY, len(self._data) // 2))
        self._left = (self._left - 1) % len(self._data)
        result = self._data[self._left]
        self._data[self._left] = None
        self._size -= 1
        return result

    def pop(self):
        if len(self) < 1:
            raise Empty("Deque is empty!")
        if self._maxlen is None and len(self._data) // 4 > len(self) > CollectionsDeque._DEFAULT_CAPACITY:
            self._resize(max(CollectionsDeque._DEFAULT_CAPACITY, len(self._data) // 2))
        self._right = (self._right + 1) % len(self._data)
        result = self._data[self._right]
        self._data[self._right] = None
        self._size -= 1
        return result

    def __getitem__(self, index):
        if index >= 0:
            if index > len(self) - 1:
                return IndexError("Index {} is out of bounds for Deque of length {}.".format(index, len(self)))
            return self._data[(self._left - 1 - index) % len(self._data)]
        else:
            if index < -len(self):
                return IndexError("Index {} is out of bounds for Deque of length {}.".format(index, len(self)))
            return self._data[(self._right - index) % len(self._data)]

    def __setitem__(self, index, value):
        if index >= 0:
            if index > len(self) - 1:
                return IndexError("Index {} is out of bounds for Deque of length {}.".format(index, len(self)))
            self._data[(self._left - 1 - index) % len(self._data)] = value
        else:
            if index < -len(self):
                return IndexError("Index {} is out of bounds for Deque of length {}.".format(index, len(self)))
            self._data[(self._right - index) % len(self._data)] = value

    def clear(self):
        self._data = [None] * CollectionsDeque._DEFAULT_CAPACITY
        self._size = 0
        self._left = 0
        self._right = len(self._data) - 1

    def rotate(self, k):
        if k > 0:
            for _ in range(k):
                self._right = (self._right + 1) % len(self._data)
                self._data[self._left] = self._data[self._right]
                if len(self) < len(self._data):
                    self._data[self._right] = None
                self._left = (self._left + 1) % len(self._data)
        elif k < 0:
            for _ in range(-k):
                self._left = (self._left - 1) % len(self._data)
                self._data[self._right] = self._data[self._left]
                if len(self) < len(self._data):
                    self._data[self._left] = None
                self._right = (self._right - 1) % len(self._data)

    def remove(self, e):
        found = False
        index = self._left - 1
        for _ in range(len(self)):
            if self._data[index] == e:
                found = True
            if found:
                self._data[index] = self._data[index - 1]
            index = (index - 1) % len(self._data)
        if found:
            self._right = (self._right + 1) % len(self._data)
            self._data[self._right] = None
            self._size -= 1
        else:
            raise ValueError("{} not found in deque!".format(e))

    def count(self, e):
        count = 0
        index = self._left - 1
        for _ in range(len(self)):
            if self._data[index] == e:
                count += 1
            index = (index - 1) % len(self._data)
        return count

    def __str__(self):
        result: list[str] = [""] * len(self)
        for i in range(len(self)):
            result[i] = str(self._data[(self._left - 1 - i) % len(self._data)])

        return "[{}]".format(", ".join(result))
