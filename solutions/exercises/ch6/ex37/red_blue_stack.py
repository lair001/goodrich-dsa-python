from typing import ClassVar
from solutions.vendor.ch06.empty import Empty


class RedBlueStack:
    _DEFAULT_CAPACITY: ClassVar[int] = 10

    _data: list
    _red_size: int
    _blue_size: int
    _red: int
    _blue: int

    def __init__(self):
        self._data = [None] * RedBlueStack._DEFAULT_CAPACITY
        self._red_size = 0
        self._blue_size = 0
        self._red = 0
        self._blue = len(self._data) - 1

    def red_len(self):
        return  self._red_size

    def blue_len(self):
        return self._blue_size

    def __len__(self):
        return self.red_len() + self.blue_len()

    def is_red_empty(self):
        return self.red_len() < 1

    def is_blue_empty(self):
        return self.blue_len() < 1

    def _resize(self, cap):
        new_data = [None] * cap
        for i in range(self.red_len()):
            new_data[i] = self._data[i]

        for i in range(len(new_data) - 1, len(new_data) - self.blue_len() - 1, -1):
            new_data[i] = self._data[i - len(new_data) + len(self._data)]

        self._blue = len(new_data) - self.blue_len() - 1
        self._data = new_data

    def red_push(self, e):
        if len(self) == len(self._data):
            self._resize(2 * len(self._data))
        self._data[self._red] = e
        self._red += 1
        self._red_size += 1

    def blue_push(self, e):
        if len(self) == len(self._data):
            self._resize(2 * len(self._data))
        self._data[self._blue] = e
        self._blue -= 1
        self._blue_size += 1

    def red_pop(self):
        if self.is_red_empty():
            raise Empty("Red stack is empty!")
        if len(self._data) // 4 > len(self) > RedBlueStack._DEFAULT_CAPACITY:
            self._resize(len(self._data) // 2)
        self._red -= 1
        result = self._data[self._red]
        self._data[self._red] = None
        self._red_size -= 1
        return result

    def red_top(self):
        if self.is_red_empty():
            raise Empty("Red stack is empty!")
        return self._data[self._red - 1]

    def blue_pop(self):
        if self.is_blue_empty():
            raise Empty("Blue stack is empty!")
        if len(self._data) // 4 > len(self) > RedBlueStack._DEFAULT_CAPACITY:
            self._resize(len(self._data) // 2)
        self._blue += 1
        result = self._data[self._blue]
        self._data[self._blue] = None
        self._blue_size -= 1
        return result

    def blue_top(self):
        if self.is_blue_empty():
            raise Empty("Blue stack is empty!")
        return self._data[self._blue + 1]

    def red_str(self):
        return "[{}]".format(", ".join(map(str, self._data[:self.red_len()])))

    def blue_str(self):
        return "[{}]".format(", ".join(map(str, self._data[len(self._data)-1:len(self._data)-1-self.blue_len():-1])))
