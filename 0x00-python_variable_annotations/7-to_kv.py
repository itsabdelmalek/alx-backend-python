#!/usr/bin/env python3
"""
A module function to create a tuple from a string and the square of it.
"""

from typing import List, Tuple, Union
import typing


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Create a tuple from a string and the square of an int/float
    returns a tupple that begins with k"""
    return k, v**2
