#!/usr/bin/env python3
"""
Defines a type-annotated safe_first_element function
"""
from typing import Sequence, Any, Union


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """Returns the first element or None"""
    if lst:
        return lst[0]
    else:
        return None
