#!/usr/bin/env python3
"""
A module function to calculate the sum of a mixed list of integers and floats
"""


from typing import Union
import typing
import math


def sum_mixed_list(mxd_lst: typing.List[typing.Union[int, float]]) -> float:
    """
    Calculate the sum of a mixed list of integers and floats. and
    returns their sum as a float
    """
    return math.fsum(mxd_lst)
