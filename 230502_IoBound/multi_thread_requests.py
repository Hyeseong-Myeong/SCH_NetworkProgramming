import concurrent.futures
import requests, threading, time

thread_local = threading.local()

def get_session():
    if not hasattr(thread_local, "session"):
        thread_local.session = requests.Session()
    return thread_local.session

def download_site(url):
    session = get_session()
    with session.get(url) as response:
        print(f"Read {len(response.content)} from {url}")

def download_all_sites(sites):
    #적절한 개수의 Thread를 미리 만들어 둠(Thread pool)
    with concurrent.futures.ThreadPoolExecutor(max_workers=20) as executor:
        executor.map(download_site, sites)

if __name__ == "__main__":
    sites = [
        "https://home.sch.ac.kr/iot",
        "https://home.sch.ac.kr/bigdata"
    ] * 80
    start_time = time.time()
    download_all_sites(sites)
    duration = time.time() - start_time
    print(f"Downloaded {len(sites)} in {duration} seconds")