#!/usr/bin/env python3
'''ASYNC'''


from basic_async_syntax import wait_random
import asyncio
import typing


async def wait_n(n: int, max_delay: int) -> typing.List[float]:
    '''DEF'''
    delays = []
    for i in range(0, n):
        delays.append(await wait_random(max_delay))
    return delays
