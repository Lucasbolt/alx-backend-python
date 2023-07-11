#!/usr/bin/env python3
"""
task 1
"""

import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """
    return of all delay values.
    """
    result = await asyncio.gather(
            *list(map(lambda i: wait_random(max_delay), range(n)))
            )
    return sorted(result)
