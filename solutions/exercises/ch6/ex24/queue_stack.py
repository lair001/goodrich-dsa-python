from solutions.exercises.ch6.ex29.rotatable_array_queue import RotatableArrayQueue


class QueueStack:
    def __init__(self):
        self._queue = RotatableArrayQueue()

    def __len__(self):
        return len(self._queue)

    def is_empty(self):
        return self._queue.is_empty()

    def push(self, e):
        self._queue.enqueue(e)

    def pop(self):
        for _ in range(len(self) - 1):
            self._queue.rotate()
        return self._queue.dequeue()

    def top(self):
        for _ in range(len(self) - 1):
            self._queue.rotate()
        result = self._queue.first()
        self._queue.rotate()
        return result

    def __str__(self):
        return self._queue.__str__()
