#!/usr/bin/env python3
"""asynchronous coroutine that wait for a random with max delay"""

import asyncio
import random

async def wait_random(max_delay: int = 10) -> float:
    """asynchronous coroutine that take an integer 
       argument and wait for random delay

       Args: max_delay int

       Return: float

    """
    random_float = random.uniform(0, max_delay)
    await asyncio.sleep(random_float)
    return random_float
