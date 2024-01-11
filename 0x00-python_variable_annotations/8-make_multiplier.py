#!/usr/bin/env python3
"""
A module with a type-annotated function to create a multiplier function.
"""


from typing import Callable
import typing


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Create a function that multiplies a float by a specified multiplier.
    and returns the result of multiplying it by the specified multiplier
    """
    def my_mustiple(multiple: float) -> float:
        """creates a new multiple function"""
        return float(multiplier * multiple)

    return my_mustiple
