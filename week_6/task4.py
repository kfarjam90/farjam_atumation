# Exercise 4: Monitoring Performance
# Task: Implement a mechanism to measure the time taken by each site download individually and print it out.
# Track the start and end time for each site download within the download_site function.
# Calculate the time taken for each site download and print it out along with the site URL.


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
    start_time = time.time()  
    session = get_session()
    with session.get(url) as response:
        content_length = len(response.content)
        end_time = time.time()  
        duration = end_time - start_time  
        print(f"Read {content_length} bytes from {url} in {duration:.2f} seconds")

def download_all_sites(sites):
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://www.jython.org",
        "http://olympus.realpython.org/dice",
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")
