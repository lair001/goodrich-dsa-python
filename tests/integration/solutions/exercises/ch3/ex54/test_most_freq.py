from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH3_PATH

PATH = os_path.join(SOLUTIONS_CH3_PATH, "ex54", "most_freq")


def test():
    result = get_stdout(PATH, "[1,4,3,4,5,4,7,8,4,9]")
    assert result == "4" + newline
