import requests
from concurrent.futures import ThreadPoolExecutor, as_completed

THREAD_POOL = 80

session = requests.Session()
session.mount('https://', requests.adapters.HTTPAdapter(pool_maxsize=THREAD_POOL, max_retries=3, pool_block=True))

def send_req(url):
    try:
        return session.get(url)
    except:
        return session.get("https://google.com")

def test_all_urls(urls):
    with ThreadPoolExecutor(max_workers=THREAD_POOL) as executor:
        for response in list(executor.map(send_req, urls)):
            if response.status_code == 200 and response.url != "https://example.com/":
                print(response.url)



urls = [ "https://9anime." + chr(i) + chr(j) for i in range(ord('a'), ord('z')+1) for j in range(ord('a'), ord('z')+1) ]
test_all_urls(urls)
