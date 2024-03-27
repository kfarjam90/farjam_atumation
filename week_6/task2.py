# Exercise 2: Error Handling in asyncio
# Task: Enhance the previous script to handle exceptions gracefully using try-except blocks in the download_site function.
# Implement error handling within the download_site function using try-except blocks to catch exceptions raised during the HTTP request.
# Consider handling specific exceptions like aiohttp.ClientError for better error reporting.

import asyncio
import aiohttp
import time

async def download_site(session,url):
    try:
        async with session.get(url) as response:
            print(f"Read {response.content_length} from {url}")
            return await response.text()
    except aiohttp.ClientError as e:
        print(f'error fetching {url}:{e}')

async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:

        tasks = []
        for url in sites:
            tasks.append(asyncio.create_task(download_site(session,url)))
        
        htmls = await asyncio.gather(*tasks)
        return htmls
if __name__ == "__main__":
    sites = [
        "https://www.example.com",
        "https://www.python.org",
        "https://www.github.com",
        "https://www.google.com",
        "https://www.yahoo.com"
    ]

    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f'Download {len(sites)} sites in {duration} seconds')