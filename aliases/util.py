from aliases.ch1 import ch1_aliases

def get_alias_value(alias):
    return dict(
                **ch1_aliases
            ).get(alias, alias)