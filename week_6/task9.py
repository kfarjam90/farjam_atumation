# Exercise 9: Memory Optimization
# Task: Optimize memory usage by avoiding unnecessary data duplication or excessive resource allocation.
# Use streaming or chunked transfer encoding for large responses to minimize memory consumption.

import asyncio
import time
import aiohttp


async def download_site(session, url):
    async with session.get(url) as response:
        while True:
            chunk = await response.content.read(1024)  
            if not chunk:
                break  
            print(f"Read {len(chunk)} bytes from {url}")


async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            task = asyncio.ensure_future(download_site(session, url))
            tasks.append(task)
        await asyncio.gather(*tasks, return_exceptions=True)


if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")
