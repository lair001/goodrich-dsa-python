import pytest
from solutions.libs.decorators.dynamic.ListDecorator import ListDecorator


@pytest.fixture()
def list_fixture():
    lst = [1, 2, 3]
    return lst, ListDecorator(lst)


def test_unwrap(list_fixture):
    lst, lst_dec = list_fixture
    assert lst_dec.unwrap() is lst


def test_len(list_fixture):
    lst, lst_dec = list_fixture
    assert len(lst_dec) is len(lst)


def test_getitem(list_fixture):
    lst, lst_dec = list_fixture
    for i in range(len(lst)):
        assert lst_dec[i] is lst[i]


def test_setitem(list_fixture):
    lst, lst_dec = list_fixture
    for i in range(len(lst)):
        new_value = lst[i] + 100
        lst_dec[i] = new_value
        assert lst_dec[i] is new_value
        assert lst[i] is new_value


def test_iteration(list_fixture):
    lst, lst_dec = list_fixture
    i = 0
    for val in lst_dec:
        assert val is lst_dec[i]
        assert val is lst[i]
        i += 1


def test_swap(list_fixture):
    lst, lst_dec = list_fixture
    for i in range(len(lst)):
        for j in range(len(lst)):
            org_val_at_i = lst[i]
            org_val_at_j = lst[j]

            lst_dec.swap(i, j)

            assert lst_dec[i] is org_val_at_j
            assert lst_dec[j] is org_val_at_i
            assert lst[i] is org_val_at_j
            assert lst[j] is org_val_at_i
