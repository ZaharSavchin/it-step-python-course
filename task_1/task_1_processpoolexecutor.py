import concurrent.futures
from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    start = time()
    with concurrent.futures.ProcessPoolExecutor(max_workers=4) as executor:
        results = [executor.submit(factorial, 800) for _ in range(100000)]
        # concurrent.futures.wait(results)
        counter = 0
        for result in results:
            result.result()
            print(counter)
            counter += 1

    print(time() - start)