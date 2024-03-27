# Exercise 8: Error Handling in ThreadPoolExecutor
# Task: Implement error handling using try-except blocks within the download_site function similar to the asyncio script.
# Handle exceptions raised during HTTP requests and ensure proper error reporting and logging.

import concurrent.futures
import requests
import threading
import time


thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    try:
        with session.get(url) as response:
            response.raise_for_status()  
            print(f"Read {len(response.content)} bytes from {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":

    
    
    sites = [
        "https://www.invalid.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
