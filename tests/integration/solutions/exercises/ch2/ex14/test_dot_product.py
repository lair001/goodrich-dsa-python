from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH2_PATH

PATH = os_path.join(SOLUTIONS_CH2_PATH, "ex14", "dot_product")


def test_for_len_2_vectors():
    result = get_stdout(PATH, "[1,2]", "[3,4]")
    assert result == "11" + newline


def test_for_len_3_vectors():
    result = get_stdout(PATH, "[1,2,3]", "[4,5,6]")
    assert result == "32" + newline
