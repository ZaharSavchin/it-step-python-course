from threading import Thread
from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


def main():
    threads = [Thread(target=factorial, args=(800,)) for i in range(100000)]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


time_start = time()
main()
print(time()-time_start)
