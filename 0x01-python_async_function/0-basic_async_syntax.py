#!/usr/bin/env python3
import asyncio
import random


async def wait_random(max_delay: int = 10):
    adj_max = max_delay + 0.004
    s = random.uniform(0, adj_max)
    await asyncio.sleep(s)
    return s
