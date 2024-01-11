#!/usr/bin/env python3
"""
mapping in type annotations
"""

from typing import Any, Union, Mapping, TypeVar


T = TypeVar('T')


def safely_get_value(dct: Mapping, key: Any,
                     default: Union[T, None] = None) -> Union[Any, T]:
    """
    Safely retrieve a value from a dictionary.
    """
    if key in dct:
        return dct[key]
    else:
        return default
