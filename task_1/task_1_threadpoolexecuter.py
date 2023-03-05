from concurrent.futures import ThreadPoolExecutor
from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def main():
    with ThreadPoolExecutor(max_workers=100000) as executor:
        futures = [executor.submit(factorial, 800) for _ in range(100000)]
        for future in futures:
            future.result()


start = time()
main()
print(time() - start)