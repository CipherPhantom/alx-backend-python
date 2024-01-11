#!/usr/bin/env python3
"""
Defines a type-annotated to_kv function
"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple from the two arguments"""
    return (k, v ** 2)
