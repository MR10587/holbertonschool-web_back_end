#!/usr/bin/env python3
'''ASYNC'''


import asyncio
import random


async def wait_random(delay = 10):
    return random.uniform(0, delay)
