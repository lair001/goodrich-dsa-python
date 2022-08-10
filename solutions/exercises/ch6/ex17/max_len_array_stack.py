from solutions.exercises.ch6.ex16.full import Full
from solutions.vendor.ch06.empty import Empty


class MaxLenArrayStack():
    def __init__(self, maxlen=None):
        self._maxlen = maxlen
        self._n = 0
        self._data = [] if maxlen is None else [None] * maxlen

    def __len__(self):
        return self._n

    def is_empty(self):
        return len(self) == 0

    def push(self, e):
        if len(self) == self._maxlen:
            raise Full("Can't push onto a full stack!")
        if self._maxlen is None:
            self._data.append(e)
        else:
            self._data[self._n] = e
        self._n += 1

    def top(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        return self._data[self._n - 1]

    def pop(self):
        if self.is_empty():
            raise Empty('Stack is empty')
        if self._maxlen is None:
            result = self._data.pop()
        else:
            result = self._data[self._n - 1]
            self._data[self._n - 1] = None
        self._n -= 1
        return result

    def __str__(self):
        return self._data.__str__()
