#!/usr/bin/env python3
"""
Defines a type-annotated sum_mixed_list function
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns the sum a list of floats and integers"""
    return sum(mxd_lst)
