#!/usr/bin/env python3
'''Generators'''


import asyncio
import time
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    start = time.perf_counter()
    asyncio.gather(await async_comprehension() async for i in range(4))
    elapsed = time.perf_counter() - start
    return elapsed
