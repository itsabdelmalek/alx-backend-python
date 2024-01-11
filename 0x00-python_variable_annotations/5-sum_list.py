#!/usr/bin/env python3
"""
A module with a type-annotated function to calculate the sum of list of floats
"""

import typing


def sum_list(input_list: typing.List[float]) -> float:
    """ returns The sum of the input list of floats"""
    return sum(input_list)
