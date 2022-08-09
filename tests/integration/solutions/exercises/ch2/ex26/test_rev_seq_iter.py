from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout
from solutions.libs.utils.path import SOLUTIONS_CH2_PATH

PATH = os_path.join(SOLUTIONS_CH2_PATH, "ex26", "rev_seq_iter")


def test_for_len_5_list():
    result = get_stdout(PATH, "[1,2,3,4,5]")
    assert result == "[5, 4, 3, 2, 1]" + newline
