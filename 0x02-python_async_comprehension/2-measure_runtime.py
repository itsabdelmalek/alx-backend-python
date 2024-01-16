#!/usr/bin/env python3
"""
An asynchronous coroutine that measures the total runtime of executing
async_comprehension four times in parallel.
"""


import asyncio
from time import perf_counter
from typing import List

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """
    Coroutine that measures the total runtime of executing
    async_comprehension four times in parallel.

    Returns:
    - float: The total runtime in seconds.
    """
    run_time = perf_counter()
    end_time = [asyncio.create_task(async_comprehension()) for i in range(4)]
    await asyncio.gather(*end_time)
    elapseed = perf_counter() - run_time
    return elapseed
