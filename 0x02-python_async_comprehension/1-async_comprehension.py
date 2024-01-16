#!/usr/bin/env python3
"""
An asynchronous coroutine collects 10 random numbers using async comprehension
"""

import asyncio
from typing import List

async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> List[float]:
    """
    Coroutine that collects 10 random numbers using async comprehension.

    Returns:
    - List[int]: A list containing 10 random numbers.
    """
    return [i async for i in async_generator()]
