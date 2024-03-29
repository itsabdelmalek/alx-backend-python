#!/usr/bin/env python3
""" regular import function """
import asyncio
import time


wait_random = __import__('0-basic_async_syntax').wait_random


def task_wait_random(max_delay: int = 0) -> asyncio.Task:
    """
    returns: asyncio Task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
