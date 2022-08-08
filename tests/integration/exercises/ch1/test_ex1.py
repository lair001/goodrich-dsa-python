from os import path as os_path
from os import linesep as newline
from tests.libs.utils.shell import get_stdout_for_cmd
from solutions.libs.utils.path import SOLUTIONS_CH1

_USING_MODULO_PATH = os_path.join(SOLUTIONS_CH1, "ex1", "using_modulo")
_WITHOUT_MODULO_PATH = os_path.join(SOLUTIONS_CH1, "ex1", "without_modulo")


def test_using_modulo_when_multiple():
    cmd = ["python", _USING_MODULO_PATH, "4", "2"]
    result = get_stdout_for_cmd(cmd)
    assert result == "4 is a multiple of 2." + newline


def test_using_modulo_when_not_multiple():
    cmd = ["python", _USING_MODULO_PATH, "5", "3"]
    result = get_stdout_for_cmd(cmd)
    assert result == "5 is not a multiple of 3." + newline


def test_without_modulo_when_multiple():
    cmd = ["python", _WITHOUT_MODULO_PATH, "4", "2"]
    result = get_stdout_for_cmd(cmd)
    assert result == "4 is a multiple of 2." + newline


def test_without_modulo_when_not_multiple():
    cmd = ["python", _WITHOUT_MODULO_PATH, "5", "3"]
    result = get_stdout_for_cmd(cmd)
    assert result == "5 is not a multiple of 3." + newline
