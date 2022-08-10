from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH6_PATH

PATH = os_path.join(SOLUTIONS_CH6_PATH, "ex18", "reverse")


def test():
    result = get_stdout(PATH)
    assert result == "S: [{}]".format(", ".join(str(i) for i in range(10))) + newline +\
           "Reversing S ..." + newline + "S: [{}]".format(", ".join(str(i) for i in range(9, -1, -1))) + newline
