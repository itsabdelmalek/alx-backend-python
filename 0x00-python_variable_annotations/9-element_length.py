#!/usr/bin/env python3
"""
duct type function
"""

from typing import Iterable, Sequence, List, Tuple
import typing


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """iterating the list"""
    return [(i, len(i)) for i in lst]
