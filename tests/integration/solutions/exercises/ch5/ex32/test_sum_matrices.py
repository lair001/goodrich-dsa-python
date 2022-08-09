from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout_for_cmd
from solutions.libs.utils.path import SOLUTIONS_CH5_PATH

PATH = os_path.join(SOLUTIONS_CH5_PATH, "ex32", "sum_matrices")


def test():
    cmd = ["pipenv", "run", "python", PATH, "[[[1,2],[3,4]],[[5,6],[7,8]]]", "[[[1,2],[3,4]],[[5,6],[7,8]]]"]
    result = get_stdout_for_cmd(cmd)
    assert result == "[[[2, 4], [6, 8]], [[10, 12], [14, 16]]]" + newline
