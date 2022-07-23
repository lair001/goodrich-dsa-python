from solutions.libs.decorators.dynamic.DynamicDecorator import DynamicDecorator
from typing import Sequence
from abc import ABCMeta, abstractstaticmethod


class SequenceDecorator(DynamicDecorator, metaclass=ABCMeta):

    @abstractstaticmethod
    def _is_valid_wrappee(potential_seq):
        return isinstance(potential_seq, Sequence)
