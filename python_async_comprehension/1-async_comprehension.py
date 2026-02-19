#!/usr/bin/env python3
'''Generators'''


import asyncio
import typing
async_generator = __import__('0-async_generator').async_generator


async def async_comprehension() -> typing.List[float]:
    result = [i async for i in await async_generator()]
    return result
