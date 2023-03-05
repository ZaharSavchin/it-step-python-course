import requests
import concurrent.futures
import time


def check_wikipedia_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return f"{url} - страница существует"
    elif response.status_code == 400:
        return f"{url} - страница не существует"


urls = [
    "https://ru.wikipedia.org/wiki/Python",
    "https://ru.wikipedia.org/wiki/Java",
    "https://ru.wikipedia.org/wiki/JavaScript",
    "https://ru.wikipedia.org/wiki/PHP",
    "https://ru.wikipedia.org/wiki/Ruby",
]

# Без использования ThreadPoolExecutor
start_time = time.time()
results = []
for url in urls:
    result = check_wikipedia_page(url)
    results.append(result)
    print(result)
print(f"Время выполнения без ThreadPoolExecutor: {time.time() - start_time} сек.")

# С использованием ThreadPoolExecutor
start_time = time.time()
results = []
with concurrent.futures.ThreadPoolExecutor() as executor:
    futures = [executor.submit(check_wikipedia_page, url) for url in urls]
    for future in concurrent.futures.as_completed(futures):
        result = future.result()
        results.append(result)
        print(result)
print(f"Время выполнения с ThreadPoolExecutor: {time.time() - start_time} сек.")
