from aliases.ch1 import ch1_aliases

all = dict(**ch1_aliases)

def substitute(argv_1):
    return all.get(argv_1, argv_1)