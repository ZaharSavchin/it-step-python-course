from time import time


def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)


def main():
    for i in range(100000):
        factorial(800)


start = time()
main()
print(time() - start)
