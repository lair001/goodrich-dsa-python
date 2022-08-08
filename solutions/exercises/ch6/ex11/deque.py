from collections import deque

class Deque:
    def __init__(self):
        self._data = deque()

    def __len__(self):
        return self._data.__len__()

    def is_empty(self):
        return len(self) == 0

    def add_first(self, ele):
        self._data.appendleft(ele)

    def add_last(self, ele):
        self._data.append(ele)

    def delete_first(self):
        return self._data.popleft()

    def delete_last(self):
        return self._data.pop()

    def first(self):
        return self._data[0]

    def last(self):
        return self._data[-1]

    def __str__(self):
        return self._data.__str__().lstrip('deque(').rstrip(')')
