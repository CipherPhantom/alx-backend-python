#!/usr/bin/env python3
"""
Defines a type-annotated safely_get_value function
"""
from typing import Mapping, Any, Union, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """Returns the value of a key in a dictionary or None"""
    if key in dct:
        return dct[key]
    else:
        return default
