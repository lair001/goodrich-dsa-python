import sys, re
from os import linesep as newline
from collections import deque

_openings = ['[', '{', '(', '<']
_openings_to_closings = {
    '[': ']',
    '{': '}',
    '(': ')',
    '<': '>'
}


def parse_list(starting_argv_index=1, starting_arg_index=0):
    seq = []
    current_argv_index = starting_argv_index
    opening = None
    closing = None

    demarcators = [" ", ",", newline]

    while True:
        arg = sys.argv[current_argv_index]
        token = []
        for i in range(starting_arg_index if current_argv_index == starting_argv_index else 0, len(arg)):
            if arg[i] in demarcators:
                if len(token) > 0:
                    seq.append(''.join(token))
                    token = []
                continue
            if arg[i] in _openings:
                if opening is None:
                    opening = arg[i]
                    closing = _openings_to_closings[opening]
                else:
                    return None, current_argv_index + (1 if i == len(arg) - 1 else 0)
            elif arg[i] == closing:
                if len(token) > 0:
                    seq.append(''.join(token))
                return seq, current_argv_index + (1 if i == len(arg) - 1 else 0)
            else:
                token.append(arg[i])
        if len(token) > 0:
            seq.append(''.join(token))
        current_argv_index += 1


def parse_int_list(starting_argv_index):
    return _parse_list_of_type(starting_argv_index, 0, int)


def parse_float_list(starting_argv_index):
    return _parse_list_of_type(starting_argv_index, 0, int)


def _parse_list_of_type(starting_argv_index, starting_arg_index, _type):
    raw = parse_list(starting_argv_index, starting_arg_index)
    return raw if raw[0] is None else (list(map(_type, raw[0])), raw[1])


def parse_int_matrix(beginning_index):
    return _parse_matrix_of_type(beginning_index, int)


def _parse_matrix_of_type(starting_argv_index, type):
    current_argv_index = starting_argv_index
    max_argv_index = current_argv_index
    openings_info = []
    lists = []
    while current_argv_index < len(sys.argv):
        arg = sys.argv[current_argv_index]
        for i in range(len(arg)):
            if arg[i] in _openings:
                openings_info.append((arg[i], current_argv_index, i))
                lists.append([])
                if len(lists) > 1:
                    lists[-2].append(lists[-1])
            if arg[i] == _openings_to_closings[openings_info[-1][0]]:
                opening, opening_argv_index, opening_arg_index = openings_info.pop()
                curr, current_argv_index = _parse_list_of_type(opening_argv_index, opening_arg_index, type)
                max_argv_index = max(max_argv_index, current_argv_index)
                if curr is None:
                    if len(lists) == 1:
                        while max_argv_index < len(sys.argv) and sys.argv[max_argv_index] == _openings_to_closings[opening]:
                            max_argv_index += 1
                        return lists[0], max_argv_index + (1 if current_argv_index == max_argv_index else 0)
                    else:
                        lists.pop()
                        current_argv_index = max_argv_index + (1 if i == len(arg) - 1 else 0)
                else:
                    lists.pop().extend(curr)
            elif i == len(arg) - 1:
                current_argv_index += 1
                max_argv_index = max(max_argv_index, current_argv_index)
 #   return lists[0], max_argv_index
