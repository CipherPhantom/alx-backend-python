#!/usr/bin/env python3
"""
Defines a task_wait_n function
"""
import asyncio
from typing import List

task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the task_wait_random function n number of times and
    Returns the list of all the delays (float values)."""
    tasks = (task_wait_random(max_delay) for _ in range(n))

    return sorted(await asyncio.gather(*tasks))
