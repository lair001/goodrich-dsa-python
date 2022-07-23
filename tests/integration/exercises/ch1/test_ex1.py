from os import path as os_path
from tests.libs.utils.shell import get_stdout_for_cmd


def test_using_modulo_when_multiple():
    cmd = [os_path.join("solutions", "exercises", "R", "ch1", "ex1", "using_modulo"), "4", "2"]
    print(cmd)
    result = get_stdout_for_cmd(cmd)
    assert result == "4 is a multiple of 2.\n"


def test_using_modulo_when_not_multiple():
    cmd = [os_path.join("solutions", "exercises", "R", "ch1", "ex1", "using_modulo"), "5", "3"]
    result = get_stdout_for_cmd(cmd)
    assert result == "5 is not a multiple of 3.\n"


def test_without_modulo_when_multiple():
    cmd = [os_path.join("solutions", "exercises", "R", "ch1", "ex1", "without_modulo"), "4", "2"]
    result = get_stdout_for_cmd(cmd)
    assert result == "4 is a multiple of 2.\n"


def test_without_modulo_when_not_multiple():
    cmd = [os_path.join("solutions", "exercises", "R", "ch1", "ex1", "without_modulo"), "5", "3"]
    result = get_stdout_for_cmd(cmd)
    assert result == "5 is not a multiple of 3.\n"
