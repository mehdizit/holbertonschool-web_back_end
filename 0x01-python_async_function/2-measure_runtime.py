#!/usr/bin/env python3
"""Measures elapsed time """

import asyncio
import random
import time


wait_n = __import__('1-concurrent_coroutines').wait_n

def measure_time(n: int, max_delay: int) -> float:
    """Returns total_time / n for wait_n() execution
       Args: n int, max_delay int
       Return: float
    """

    elapsed_time: float
    start_time = time.time()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(wait_n(n, max_delay))
    elapsed_time = time.time() - start_time
    return elapsed_time / n
