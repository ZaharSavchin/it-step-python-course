from multiprocessing import Process
from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    start = time()
    processes = [Process(target=factorial, args=(800,)) for i in range(100)]
    for process in processes:
        process.start()
    for process in processes:
        process.join()
    print(time()-start)