#!/usr/bin/env python3
"""
Defines a type-annotated element_length function
"""
from typing import Iterator, Sequence, List, Tuple


def element_length(lst: Iterator[Sequence]) -> List[Tuple[Sequence, int]]:
    """Returns a list of tuples"""
    return [(i, len(i)) for i in lst]
