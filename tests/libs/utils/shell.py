import subprocess
from tests.libs.utils.string import bytes_to_str


def get_stdout(path, *args):
    return _get_stdout_for_cmd(["pipenv", "run", "python", path, *args])


def _get_stdout_for_cmd(cmd):
    return bytes_to_str(subprocess.run(cmd, stdout=subprocess.PIPE).stdout)
