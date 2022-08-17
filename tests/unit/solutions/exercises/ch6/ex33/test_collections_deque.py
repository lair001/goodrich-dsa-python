from solutions.exercises.ch6.ex33.collections_deque import CollectionsDeque


def test_get_negative_indices():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)

    for i in range(1, 9):
        assert deque[-i] == 8 - i


def test_set_positive_indices():
    deque = CollectionsDeque()
    for _ in range(8):
        deque.append(-128)
    for i in range(8):
        deque[i] = i
    for i in range(8):
        assert deque[i] == i


def test_clear():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)
    deque.clear()
    assert len(deque) == 0
    assert deque.is_empty() is True

    for i in range(8):
        deque.append(i)
    for i in range(8):
        assert deque[i] == i


def test_rotate_right():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)
    deque.rotate(4)
    for i in range(4):
        assert deque[i] == i + 4
        assert deque[i + 4] == i


def test_rotate_left():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)
    deque.rotate(-4)
    for i in range(4):
        assert deque[i] == i + 4
        assert deque[i + 4] == i


def test_set_negative_indices():
    deque = CollectionsDeque()
    for _ in range(8):
        deque.append(-128)
    for i in range(1, 9):
        deque[-i] = i
    for i in range(1, 9):
        assert deque[-i] == i


def test_remove():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)
        if i == 3:
            deque.append(7)

    deque.remove(7)
    assert len(deque) == 8
    for i in range(8):
        assert deque[i] == i


def test_count():
    deque = CollectionsDeque()
    for i in range(8):
        deque.append(i)
        deque.append(8)
    assert deque.count(8) == 8


def test_maxlen_deque():
    deque = CollectionsDeque(8)
    for i in range(16):
        deque.append(i)

    for i in range(8):
        assert deque[i] == i + 8

    for i in range(16, 24):
        deque.appendleft(i)

    for i in range(8):
        assert deque[i] == 23 - i
