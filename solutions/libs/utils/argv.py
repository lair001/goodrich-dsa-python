import sys, re


def parse_list(beginning_index):
    seq = []
    current_index = beginning_index
    opening = None
    closing = None
    openings = ['[', '{', '(']
    openings_to_closings = {
        '[': ']',
        '{': '}',
        '(': ')',
        '<': '>'
    }
    blanks = [" ", ""]

    while True:
        arg = sys.argv[current_index]
        clean_arg = arg
        current_index += 1
        if opening == None:
            if arg[0] in openings:
                opening = arg[0]
                clean_arg = re.sub("\A%s" %(re.escape(opening)), '', clean_arg)
                closing = openings_to_closings[opening]
                cleaning_pattern = "(,|%s\Z)" %(re.escape(closing))
            else:
                continue
        clean_arg = re.sub(cleaning_pattern, ' ', clean_arg)
        for token in clean_arg.split(" "):
            if token not in blanks:
                seq.append(token)
        if arg[-1] == closing:
            break
    return seq, current_index


def parse_int_list(beginning_index):
    raw = parse_list(beginning_index)
    return list(map(int, raw[0])), raw[1]