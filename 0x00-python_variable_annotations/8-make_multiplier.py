#!/usr/bin/env python3
"""
Defines a type-annotated make_multiplier function
"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """Returns a function that multiplies a float by multiplier"""
    def func(num: float) -> float:
        """Return the multiplication of multiplier and a float"""
        return num * multiplier
    return func
