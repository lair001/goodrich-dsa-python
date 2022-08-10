from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH4_PATH

PATH = os_path.join(SOLUTIONS_CH4_PATH, "ex16", "reverse_str")


def test():
    result = get_stdout(PATH, "Why my eye?")
    assert result == "?eye ym yhW" + newline
