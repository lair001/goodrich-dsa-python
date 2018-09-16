from abc import ABCMeta, abstractstaticmethod


class DynamicDecorator(metaclass=ABCMeta):

    def unwrap(self):
        """Exposes the decorated object. Uses include passing type checks."""
        return self.__dict__['_wrappee']

    @abstractstaticmethod
    def _is_valid_wrappee(potential_wrappee):
        return True

    def __init__(self, wrappee):
        assert self._is_valid_wrappee(wrappee)
        self._wrappee = wrappee

    def __iter__(self):
        return self.unwrap().__iter__()

    def __next__(self):
        return self.unwrap().__next__()

    def __getattr__(self, item):
        return getattr(self.unwrap(), item)

    def __setattr__(self, key, value):
        if key == '_wrappee':
            self.__dict__[key] = value
        else:
            setattr(self.unwrap(), key, value)

    def __delattr__(self, item):
        delattr(self.unwrap(), item)

    def __len__(self):
        return len(self.unwrap())

    def __getitem__(self, item):
        return self.unwrap().__getitem__(item)

    def __setitem__(self, key, value):
        self.unwrap().__setitem__(key, value)

    def __delitem__(self, key):
        self.unwrap().__delitem__(key)

