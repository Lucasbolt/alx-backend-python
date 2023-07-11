#!/usr/bin/env python3
"""
task 0
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """wait random time """
    adj_max = max_delay + 0.004
    s = random.uniform(0, adj_max)
    await asyncio.sleep(s)
    return s
