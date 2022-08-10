from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH3_PATH

PATH = os_path.join(SOLUTIONS_CH3_PATH, "ex36", "ten_largest")


def test_for_len_20_list():
    result = get_stdout(PATH, "[{}]".format(", ".join(str(i) for i in range(20))))
    assert result == "[{}]".format(", ".join(str(i) for i in range(10, 20))) + newline
