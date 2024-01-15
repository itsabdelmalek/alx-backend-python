#!/usr/bin/env python3
"""
An asynchronous coroutine that waits for a random delay.
"""

import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """
    Wait for a random delay between 0 and max_delay seconds.
    """
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
