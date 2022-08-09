from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH5_PATH

PATH = os_path.join(SOLUTIONS_CH5_PATH, "ex31", "sum_matrix")


def test_for_2_by_2_matrix():
    result = get_stdout(PATH, "[[1,2],[3,4]]")
    assert result == "10" + newline


def test_for_2_by_2_by_2_matrix():
    result = get_stdout(PATH, "[[[1,2],[3,4]],[[5,6],[7,8]]]")
    assert result == "36" + newline
