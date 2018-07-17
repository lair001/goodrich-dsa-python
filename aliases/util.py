from aliases.ch1 import ch1_aliases
from aliases.ch2 import ch2_aliases

def get_alias_value(alias):
    return dict(
                **ch1_aliases,
                **ch2_aliases
            ).get(alias, alias)