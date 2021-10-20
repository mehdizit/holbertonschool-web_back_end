#!/usr/bin/env python3
""" measure runtime """
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """ mesure runtime """
    t = time.time()
    result = [async_comprehension() for i in range(4)]
    await asyncio.gather(*result)
    return time.time() - t
