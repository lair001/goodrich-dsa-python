from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH1_PATH

PATH = os_path.join(SOLUTIONS_CH1_PATH, "ex19", "chr_seq")


def test():
    result = get_stdout(PATH)
    assert result == "['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's'," \
                     " 't', 'u', 'v', 'w', 'x', 'y', 'z']" + newline
