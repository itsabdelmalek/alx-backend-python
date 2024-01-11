#!/usr/bin/env python3
"""
duck-type annotation
"""

from typing import Iterable, Sequence, List, Union, Any


def safe_first_element(lst: Sequence[Any]) -> Union[Any, None]:
    """
    Safely retrieve the first element from a list.
    """
    if lst:
        return lst[0]
    else:
        return None
