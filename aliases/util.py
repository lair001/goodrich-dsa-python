import glob

from os import linesep as newline
from os import path as os_path

aliases = {}


def get_alias_path(alias):
    chapter = alias.split("/")[0]
    load_aliases(chapter)

    return aliases[chapter][alias]


def get_alias_list(chapter):
    load_aliases(chapter)

    result = ""
    for chapter_aliases in aliases.values():
        result += newline
        for alias, path in chapter_aliases.items():
            result += "{:14s} {:s}".format(alias, os_path.basename(path)) + newline

    return result


def add_alias(chapter, exercise, filename):
    if chapter not in aliases.keys():
        aliases[chapter] = {}

    i = 1
    while True:
        alias = "{}/{}".format(chapter, exercise)
        if i > 1:
            alias = "{}/{}".format(alias, i)
        if alias not in aliases[chapter].keys():
            aliases[chapter][alias] = os_path.join("solutions", "exercises", chapter, exercise, filename)
            return alias
        else:
            i += 1


def load_aliases(chapter):
    if len(chapter) < 3:
        chapter = "*"
    paths = glob.glob(os_path.join("aliases", chapter + "_def.txt"))

    for path in paths:
        def_file = open(path, "r")
        chapter = os_path.basename(path).split("_")[0]
        for line in def_file:
            line.strip()
            if len(line) > 1:
                exercise, filename = line.split()
                add_alias(chapter, exercise, filename)
