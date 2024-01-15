#!/usr/bin/env python3
"""
Defines a wait_n function
"""
import asyncio
from typing import List

wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Calls the wait_random function n number of times and
    Returns the list of all the delays (float values)."""
    tasks = (wait_random(max_delay) for _ in range(n))

    return sorted(await asyncio.gather(*tasks))
