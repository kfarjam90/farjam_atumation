# Exercise 5: Concurrency Limitation
# Task: Implement a semaphore mechanism using asyncio.Semaphore to limit the maximum number of concurrent downloads.
# Acquire and release the semaphore appropriately within the download_site function to control concurrency.

import asyncio
import time
import aiohttp
import requests

semaphore = asyncio.Semaphore(10)

async def download_site(url):
    async with semaphore:
        with requests.get(url) as response:
            print("Read {0} from {1}".format(len(response.content), url))


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
    asyncio.run(download_site(sites))
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} sites in {duration} seconds")

# Downloaded 160 sites in 0.5103304386138916 seconds