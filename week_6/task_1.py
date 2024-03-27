# # Exercise 1: Basic Parallelism with asyncio
# # Task: Write a script to asynchronously download 5 websites using the asyncio module.
# # Use the asyncio module to define asynchronous functions for downloading websites (download_site) and downloading all sites concurrently (download_all_sites).
# # Execute the script using asyncio.run() or by creating an event loop with asyncio.get_event_loop().run_until_complete().
# # Exercise 2: Error Handling in asyncio

import requests
import time

# def download_site(url):
#     response = requests.get(url)
#     print(f"Read {len(response.content)} from {url}")
#     return response.text

# def download_all_sites(sites):
#     htmls = []
#     for url in sites:
#         html = download_site(url)
#         htmls.append(html)
#     return htmls

# if __name__ == "__main__":
#     sites = [
#         "https://www.example1.com",
#         "https://www.example2.org",
#         "https://www.example3.com",
#         "https://www.google.com",
#         "https://www.yahoo.com"
#     ]

#     start_time = time.time()
#     download_all_sites(sites)
#     duration = time.time() - start_time
#     print(f'Download {len(sites)} sites in {duration} seconds')

import asyncio
import aiohttp
import time

async def download_site(session,url):
    try:
        async with session.get(url) as response:
            print(f"Read {(response.content_length)} from {url}")
            return await response.text()
    except aiohttp.ClientError as e:
        print(f'error {e}')
async def download_all_sites(sites):
    async with aiohttp.ClientSession() as session:
        tasks = []
        for url in sites:
            tasks.append(asyncio.create_task(download_site(session,url)))

        await asyncio.gather(*tasks)

if __name__ == "__main__":
    sites = [
        "https://www.example1.com",
        "https://www.example2.org",
        "https://www.example3.com",
        "https://www.google.com",
        "https://www.yahoo.com"
    ]

    start_time = time.time()
    asyncio.run(download_all_sites(sites))
    duration = time.time() - start_time
    print(f'Download {len(sites)} sites in {duration} seconds')




