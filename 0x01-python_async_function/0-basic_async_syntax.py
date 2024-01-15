#!/usr/bin/env python3
"""
Defines a wait_random function
"""
import random
import asyncio


async def wait_random(max_delay: int = 10) -> float:
    """Waits for a random delay between 0 and max_delay
    (included and float value) seconds and eventually returns it."""
    delay: float = random.uniform(0, max_delay)
    await asyncio.sleep(delay)

    return delay
