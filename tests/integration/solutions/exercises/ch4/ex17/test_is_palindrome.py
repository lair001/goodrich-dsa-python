from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH4_PATH

PATH = os_path.join(SOLUTIONS_CH4_PATH, "ex17", "is_palindrome")


def test_for_palindrome():
    result = get_stdout(PATH, "gohangasalamiimalasagnahog")
    assert result == "True" + newline


def test_for_non_palindrome():
    result = get_stdout(PATH, "wendy")
    assert result == "False" + newline
