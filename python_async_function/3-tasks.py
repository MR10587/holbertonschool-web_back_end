#!/usr/bin/env python3
'''Tasks'''


wait_random = __import__('0-basic_async_syntax').wait_random
import asyncio


def task_wait_random(max_delay: int):
    '''Wait random for task'''
    async def tasks():
        return await asyncio.run(wait_random(max_delay))
    return asyncio.run(tasks())
