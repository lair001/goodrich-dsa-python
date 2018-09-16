from abc import ABCMeta, abstractstaticmethod


class DynamicDecorator(metaclass=ABCMeta):

    def __init__(self, wrappee):
        assert self._is_valid_wrappee(wrappee)
        self._wrappee = wrappee

    def __iter__(self):
        self._wrappee.__iter__()

    def __next__(self):
        self._wrappee.__next__()

    def __getattr__(self, item):
        return getattr(self._wrappee, item)

    def __setattr__(self, key, value):
        if key == '_wrappee':
            self.__dict__[key] = value
        else:
            setattr(self._wrappee, key, value)

    def __delattr__(self, item):
        delattr(self.__wrappee, item)

    def unwrap(self):
        """Exposes the decorated object. Uses include passing type checks."""
        return self._wrappee

    @abstractstaticmethod
    def _is_valid_wrappee(potential_wrappee):
        return True
