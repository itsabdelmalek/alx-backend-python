#!/usr/bin/env python3
"""
An asynchronous coroutine that yields random numbers.
"""

import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """
    Coroutine that loops 10 times, asynchronously waits 1 second,
    and yields a random number between 0 and 10.

    Yields:
    - int: A random number between 0 and 10.
    """
    for _ in range(10):
        await asyncio.sleep(1)
        yield random.random() * 10
