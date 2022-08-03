import sys, re
from collections import deque

_openings = ['[', '{', '(', '<']
_openings_to_closings = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}


def parse_list(beginning_index):
    seq = []
    current_index = beginning_index
    opening = None
    closing = None

    blanks = [" ", ""]

    while True:
        arg = sys.argv[current_index]
        clean_arg = arg
        current_index += 1
        if opening is None:
            if arg[0] in _openings:
                opening = arg[0]
                clean_arg = re.sub(r"\A%s" % (re.escape(opening)), '', clean_arg)
                closing = _openings_to_closings[opening]
                cleaning_pattern = r"(,|%s\Z)" % (re.escape(closing))
            else:
                continue
        clean_arg = re.sub(cleaning_pattern, ' ', clean_arg)
        for token in clean_arg.split(" "):
            if token in _openings:
                return (None, current_index)
            if token not in blanks:
                seq.append(token)
        if arg[-1] == closing:
            break
    return seq, current_index


def parse_int_list(beginning_index):
    return _parse_list_of_type(beginning_index, int)


def parse_float_list(beginning_index):
    return _parse_list_of_type(beginning_index, int)


def _parse_list_of_type(beginning_index, type):
    raw = parse_list(beginning_index)
    return raw if raw[0] is None else (list(map(type, raw[0])), raw[1])


def parse_int_matrix(beginning_index):
    return _parse_matrix_of_type(beginning_index, int)


def _parse_matrix_of_type(beginning_index, type):
    current_index = beginning_index
    max_index = current_index
    openings_info = []
    lists = []
    while True:
        arg = sys.argv[current_index]
        if arg[0] in _openings:
            openings_info.append((arg[0], current_index))
            lists.append([])
            if len(lists) > 1:
                lists[-2].append(lists[-1])
        if arg[-1] == _openings_to_closings[openings_info[-1][0]]:
            opening_index = openings_info.pop()[1]
            curr, current_index = _parse_list_of_type(opening_index, type)
            max_index = max(max_index, current_index)
            if curr is None:
                if len(lists) == 1:
                    return lists[0], max_index + 1
                else:
                    lists.pop()
                    current_index = max_index + 1
            else:
                lists.pop().extend(curr)
        else:
            current_index += 1
            max_index = max(max_index, current_index)
