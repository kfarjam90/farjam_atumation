# Exercise 3: Increasing Concurrency
# Task: Modify the ThreadPoolExecutor to have a higher value for max_workers parameter (e.g., 10) to increase concurrency.
# Ensure that the system can handle the increased concurrency level without exhausting resources such as CPU or memory

import asyncio
import aiohttp

# async def download_site(semaphore, session, url):
#     async with semaphore:
#         async with session.get(url) as response:

