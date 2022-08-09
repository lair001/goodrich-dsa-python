from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH1_PATH

PATH = os_path.join(SOLUTIONS_CH1_PATH, "ex1", "using_modulo")


def test_when_multiple():
    result = get_stdout(PATH, "4", "2")
    assert result == "4 is a multiple of 2." + newline


def test_when_not_multiple():
    result = get_stdout(PATH, "5", "3")
    assert result == "5 is not a multiple of 3." + newline
