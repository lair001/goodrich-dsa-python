import string

from aliases.ch1 import ch1_aliases
from aliases.ch2 import ch2_aliases
from os import linesep as newline
from os import path as os_path

def get_alias_value(alias):
    return dict(
                **ch1_aliases,
                **ch2_aliases
            ).get(alias, alias)

def get_alias_list(chapter):
    match chapter:
        case "ch1":
            aliases = ch1_aliases
        case "ch2":
            aliases = ch2_aliases
        case _:
            aliases = dict(
                **ch1_aliases,
                **ch2_aliases
            )

    result = ""
    for key, val in aliases.items():
        result += "{:14s} {:s}".format(key, os_path.basename(val)) + newline

    return result