from solutions.libs.decorators.dynamic.SequenceDecorator import SequenceDecorator


class ListDecorator(SequenceDecorator):

    @staticmethod
    def _is_valid_wrappee(potential_list):
        return isinstance(potential_list, list)

    def swap(self, i, j):
        """Swap elements at indices i and j."""
        temp = self._wrappee[i]
        self._wrappee[i] = self._wrappee[j]
        self._wrappee[j] = temp
